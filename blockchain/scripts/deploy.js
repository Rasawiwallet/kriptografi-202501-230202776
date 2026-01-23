onst hre = require("hardhat");


async function main() {
const TinyCoin = await hre.ethers.getContractFactory("TinyCoin");
const tinyCoin = await TinyCoin.deploy(1000000); // 1 juta TINY


await tinyCoin.waitForDeployment();


console.log("TinyCoin deployed to:", await tinyCoin.getAddress());
}


main().catch((error) => {
console.error(error);
process.exitCode = 1;
});