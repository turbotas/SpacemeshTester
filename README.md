SpacemeshTester.sikuli

This small and badly written Sikulix script makes transactions on Spacemesh using Sikulix to control the Spacemesh GUI (not using Spacemesh API calls).

Ideal usecase is that you use two of these running on different wallets to bounce SMH between test accounts. If you fail to provide a destination wallet address, it will default to a wallet that you do not control!

You will need the Spacemesh Gui and Sikulix installed to use this test script.

At startup, it provides three dialogs for where to send, how many transactions, and how long to pause each transaction.

If you fail to set a destination Spacemesh address, it will send to me, so don't leave that dialog empty!

Current status: Runs and has the beginnings of some advanced functions, but they are not written yet!  If the Spacemesh Client is not Running, Logged in and running on a Spawned account, then the script will not work.

Warning: This tool deliberately makes Spacemesh transactions from your wallet.  You should not run this script unless you understand the risks that this would entail!

TurboTas 2023

