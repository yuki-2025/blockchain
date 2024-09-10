import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from blockchain import Blockchain

# Use the full page width
st.set_page_config(layout="wide")

# Initialize session state
if 'blockchain' not in st.session_state:
    st.session_state.blockchain = Blockchain()

# Streamlit app
st.title("Blockchain Payment Visualization")

# Create two columns for layout with adjusted ratios
col1, col2 = st.columns([3, 2])

# Sidebar for adding transactions
with st.sidebar:
    st.header("Add Transaction")
    sender = st.text_input("Sender")
    recipient = st.text_input("Recipient")
    amount = st.number_input("Amount", min_value=0.01, step=0.01)

    if st.button("Add Transaction"):
        transaction = {
            "sender": sender,
            "recipient": recipient,
            "amount": amount
        }
        st.session_state.blockchain.add_new_transaction(transaction)
        st.success("Transaction added successfully!")

    if st.button("Mine Block"):
        if not st.session_state.blockchain.unconfirmed_transactions:
            st.warning("No transactions to mine.")
        else:
            try:
                result = st.session_state.blockchain.mine()
                if result:
                    st.success(f"Block #{result} mined successfully!")
                else:
                    st.warning("Mining failed. Please try again.")
            except Exception as e:
                st.error(f"An error occurred during mining: {str(e)}")

# Visualization of transactions (left column)
with col1:
    st.header("Transaction Visualization")

    G = nx.DiGraph()
    for block in st.session_state.blockchain.chain:
        for tx in block.transactions:
            G.add_edge(tx['sender'], tx['recipient'], weight=tx['amount'])

    if G.number_of_nodes() > 0:
        pos = nx.spring_layout(G)
        fig, ax = plt.subplots(figsize=(12, 8))
        nx.draw(G, pos, ax=ax, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_weight='bold')
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)
        ax.set_title("Transaction Network", fontsize=16)
        st.pyplot(fig)
    else:
        st.write("No transactions to visualize yet.")

    # Display unconfirmed transactions
    st.header("Unconfirmed Transactions")
    if st.session_state.blockchain.unconfirmed_transactions:
        for tx in st.session_state.blockchain.unconfirmed_transactions:
            st.write(f"- {tx['sender']} sent {tx['amount']} to {tx['recipient']}")
    else:
        st.write("No unconfirmed transactions.")

# Display blockchain (right column)
with col2:
    st.header("Blockchain")
    
    for i, block in enumerate(st.session_state.blockchain.chain):
        color = "#e6f3ff" if i % 2 == 0 else "#e6ffe6"  # Alternate between light blue and light green
        with st.container():
            st.markdown(f"""
                <div style="
                    background-color: {color};
                    padding: 10px;
                    border-radius: 5px;
                    margin-bottom: 10px;
                    border: 1px solid #d0d0d0;
                ">
                    <h3>Block #{block.index}</h3>
                    <p>Timestamp: {block.timestamp}</p>
                    <p>Previous Hash: {block.previous_hash[:20]}...</p>
                    <p>Hash: {block.hash[:20]}...</p>
                    <p>Transactions: {len(block.transactions)}</p>
                </div>
            """, unsafe_allow_html=True)
            
            if block.transactions:
                with st.expander("View Transactions"):
                    for tx in block.transactions:
                        st.write(f"- {tx['sender']} sent {tx['amount']} to {tx['recipient']}")
        
        st.write("")  # Add some space between blocks