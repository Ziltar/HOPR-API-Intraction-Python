from hoprApi import *
import random, time

def main():
    while True:
        doStuff()
        print("Waiting 60 minutes....")
        time.sleep(3600)
        

def doStuff():
    random_peers = getRandomPeers(get_peers(), 10)
    openChannels(random_peers, 0.1)
    sendMessages(random_peers, "Hello!")
    print("Waiting 7 minutes....")
    time.sleep(490)
    sendHopMessages(random_peers)
    closeChannels(random_peers)
   
def getRandomPeers(peers, amount):
    random_peers = []
    while (len(random_peers) < 10):
        peer = random.choice(peers[0]['connected'])['peerId']
        ping_l = ping(peer)
        print(ping_l)
        if "latency" in ping_l:
            if ping_l["latency"] < 10000:
                print(True)
                random_peers.append(peer)       
    return random_peers

def sendMessages(peers, msg):
    print("Sending MSGs:")
    for peer in peers:
        print(peer + "--->" + send_message(peer, msg, []))

def sendHopMessages(peers):
    print("Sending MSGs:")
    for peer in peers:
        print("me--->"+peer+"--->me")
        print(send_message(NODE_HOPR_ADR, "Test", [peer] ))

def openChannels(peers, amount):
    for peer in peers:
        print("Opening channel: " + peer)
        openChannel(peer, amount)

def closeChannels(peers):
    for peer in peers:
        print("Closing channel: " + peer)
        close_Channel(peer)

if __name__ == "__main__":
    main()

