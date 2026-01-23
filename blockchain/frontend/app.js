let provider;
let signer;
let contract;
const contractAddress = "0x620eF038b50A01aF8Ed25f1F81fFa7Ed3c05c78E";
const abi = [
"function transfer(address to, uint256 amount) public returns (bool)"
];
async function connectWallet() {
if (!window.ethereum) return alert("Install MetaMask dulu");
provider = new ethers.BrowserProvider(window.ethereum);
signer = await provider.getSigner();
contract = new ethers.Contract(contractAddress, abi, signer);


document.getElementById("status").innerText = "Wallet connected";
}


async function sendToken() {
const to = document.getElementById("to").value;
const amount = document.getElementById("amount").value;


const tx = await contract.transfer(to, ethers.parseUnits(amount, 18));
await tx.wait();


document.getElementById("status").innerText = "Transfer berhasil";
}