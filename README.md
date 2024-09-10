# App1 - Blockchain
This app show the main features of blockchain and how they relate to key blockchain principles. It highlights important concepts like Proof of Work (PoW) and mining, which are crucial to understanding how blockchain technology operates.

The app provides an interactive way for users to engage with these concepts, making it easier to grasp the fundamentals of blockchain technology. By allowing users to add transactions, mine blocks, and visualize the resulting blockchain, it offers a practical demonstration of how a basic blockchain functions.

Demo: https://blockchain-1.streamlit.app/

![image](https://github.com/user-attachments/assets/ea50edb8-f667-4bfb-8865-d5d530ba4ea4)

![image](https://github.com/user-attachments/assets/9b7801f5-bd8a-42dd-97a5-706bca0dd36b)

# Code Explaination

Please also check The code demonstrates a basic implementation of a blockchain and the process of mining a block, integrated into a Streamlit web app for visualization purposes.

### Block Class:
**Purpose**: Represents a single block in the blockchain.<br>
**Key Functions**: 
1. **Stores Transactions**: Contains the list of transactions that will be added to the blockchain.
2. **Computes Hash**: The compute_hash method converts all the block's data (like transactions, timestamp, and previous hash) into a hash using the SHA-256 algorithm. This hash is used to identify the block uniquely.
3. **Tracks Nonce**: The nonce is a number that miners adjust to solve the proof-of-work puzzle (this is how they find a valid hash).

### Blockchain Class:
**Purpose**: Manages the chain of blocks and the mining process.<br>
**Key Functions**: 
1. **Genesis Block Creation**: Initializes the blockchain by creating the first block (the genesis block).
2. **Adding New Blocks**: Contains methods to verify and add new blocks to the chain after ensuring the proof-of-work has been correctly solved.
3. **Proof of Work**: The proof_of_work method adjusts the nonce until the block’s hash meets the difficulty requirement (i.e., starts with a certain number of leading zeros).
4. **Transaction Management**: Holds a pool of unconfirmed transactions that will eventually be added to a block during the mining process.
5. **Block Validation**: Ensures blocks are valid by checking their hashes and previous block connections. both the Block and Blockchain classes 

### Workflow of the Blockchain:<br>
1. **Adding a Transaction**: A user inputs the sender, recipient, and amount into the Streamlit sidebar. The transaction is then appended to the list of unconfirmed transactions in the blockchain.
2. **Mining Process**: When the "Mine Block" button is pressed, the blockchain takes all the unconfirmed transactions, groups them into a block, and begins the mining process.
The mining process involves solving a cryptographic puzzle (proof of work). It adjusts the nonce of the block until it finds a hash that matches the required difficulty (i.e., the hash starts with a certain number of leading zeros).
Once a valid hash is found, the block is added to the chain, and the unconfirmed transactions are cleared.
3. **Validation**: The block's hash is computed and validated against the proof-of-work (it must meet the difficulty criteria). This ensures that each block in the chain is tamper-resistant.

---

# App2 - Blockchain with Smart Contract
![image](https://github.com/user-attachments/assets/b7bc7254-dd93-4151-83e1-ebd5e8e9c7f3)

### SmartContract Class:
**Purpose**: Represents a smart contract that can be deployed and executed on the blockchain. 
**Key Functions**: 
1. **Stores Transactions**:  Stores the Python code that defines the contract's behavior, the address of the contract creator, and the amount of cryptocurrency held by the contract.
2. **execute**: Runs the contract's code with given parameters and updates the contract's state.

### Workflow of Smart Contracts:
1. **Contract Deployment**: Users create new contracts by providing code and an address, which are then stored in the blockchain.
2. **Contract Execution**: Users interact with deployed contracts by calling their functions with specific parameters.
3. **Mining Process**: Contract-related transactions are included in mined blocks, making them part of the blockchain's permanent record.
4. **State Persistence**: The blockchain maintains and updates the state of each contract between executions.
5. **Validation**: (In real systems) Ensures that contract operations comply with predefined rules and constraints.

### Principles Behind Blockchain:
> 1. **Decentralization**: The blockchain allows for a decentralized system where transactions are verified without the need for a central authority.
> 2. **Immutability**: Once a block is added to the blockchain, it is immutable due to the cryptographic link between the blocks (via the hash of the previous block). Any attempt to modify a block will invalidate all subsequent blocks.
> 3. **Proof of Work**: This is the consensus algorithm used in this example. The network’s nodes (miners) must perform computationally expensive work to "mine" a block, making it difficult to tamper with the chain.
> 4. **Transparency**: Each transaction and block is visible to all participants, fostering trust.
