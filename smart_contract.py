import streamlit as st
import hashlib
import json
import time

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2
        self.pending_transactions = []

    def create_genesis_block(self):
        return Block(0, [], time.time(), "0")

    def get_latest_block(self):
        return self.chain[-1]

    def mine_pending_transactions(self, miner_address):
        block = Block(len(self.chain), self.pending_transactions, time.time(), self.get_latest_block().hash)
        block.mine_block(self.difficulty)
        self.chain.append(block)
        self.pending_transactions = [
            {"from": "network", "to": miner_address, "amount": 1}
        ]

    def add_transaction(self, sender, recipient, amount):
        self.pending_transactions.append({
            "from": sender,
            "to": recipient,
            "amount": amount
        })

class SmartContract:
    def __init__(self):
        self.balance = 0
        self.owner = "contract_creator"

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"

    def withdraw(self, amount, address):
        if address != self.owner:
            return "Only the owner can withdraw"
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Withdrawn {amount}. New balance: {self.balance}"

    def get_balance(self):
        return f"Contract balance: {self.balance}"

# Initialize session state
if 'blockchain' not in st.session_state:
    st.session_state.blockchain = Blockchain()
if 'smart_contract' not in st.session_state:
    st.session_state.smart_contract = SmartContract()

st.title('Simulated Blockchain with Smart Contract')

st.info("""
        💡 Start by performing a few Smart Contract actions, such as adding a deposit or making a withdrawal. 
        \n💡 You can view pending transactions after that. Then, proceed to mine a block and check the updated blockchain state. """)

# Smart Contract interactions in sidebar
st.sidebar.header('Smart Contract')
action = st.sidebar.selectbox('Select Action', ['Deposit', 'Withdraw', 'Check Balance'])

if action == 'Deposit':
    amount = st.sidebar.number_input('Amount to deposit', min_value=0, value=0)
    if st.sidebar.button('Deposit'):
        result = st.session_state.smart_contract.deposit(amount)
        st.session_state.blockchain.add_transaction("user", "smart_contract", amount)
        st.sidebar.success(result)

elif action == 'Withdraw':
    amount = st.sidebar.number_input('Amount to withdraw', min_value=0, value=0)
    if st.sidebar.button('Withdraw'):
        result = st.session_state.smart_contract.withdraw(amount, "contract_creator")
        if "Withdrawn" in result:
            st.session_state.blockchain.add_transaction("smart_contract", "contract_creator", amount)
        st.sidebar.success(result)

elif action == 'Check Balance':
    st.sidebar.success(st.session_state.smart_contract.get_balance())

st.sidebar.markdown("---")

# Sidebar for blockchain operations and smart contract interactions
st.sidebar.header('Blockchain Operations')
if st.sidebar.button('Mine Block'):
    st.session_state.blockchain.mine_pending_transactions("miner_address")
    st.sidebar.success("Block mined successfully!")

# Display the latest block info
st.sidebar.subheader('Latest Block')
latest_block = st.session_state.blockchain.get_latest_block()
st.sidebar.json({
    "Index": latest_block.index,
    "Timestamp": latest_block.timestamp,
    "Transactions": len(latest_block.transactions),
    "Previous Hash": latest_block.previous_hash[:10] + "...",
    "Hash": latest_block.hash[:10] + "..."
})

# Main content area split into two columns
col1, spacer, col2 = st.columns([0.475, 0.05, 0.475])

with col1:
    st.header('Pending Transactions')
    st.json(st.session_state.blockchain.pending_transactions)

with col2:
    st.header('Blockchain State')
    st.json([vars(block) for block in st.session_state.blockchain.chain])