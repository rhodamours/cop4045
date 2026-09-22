def add_user(sn: dict, username: str, fullname: str) -> bool:
    if username in sn:
        return False
    else:
        sn[username] = (fullname, [])
        return True
        
def add_friend(sn: dict, user1: str, user2: str) -> bool:
    if user1 in sn and user2 in sn:
        sn[user1][1].append(user2)
        sn[user2][1].append(user1)
        
        return True
    else:
        return False

def get_friends(sn: dict, user1: str, distance: int) -> list:
    if user1 in sn:
        friends = {}
        dist = 1
        
        for friend in sn[user1][1]:
            friends = friends | {friend: dist}
        
        if distance == 1:
            return [friend for friend in friends]
        
        dist += 1
        
        while dist <= distance:
            prev_dist_frs = [fr for fr in friends if friends[fr] == dist - 1]
            
            for friend in prev_dist_frs:
                for frfr in sn[friend][1]:
                    if frfr not in friends and frfr != user1:
                        friends = friends | {frfr: dist}
                    
            dist += 1
        
        return [friend for friend in friends]
    
def save_network(filename: str, sn: dict) -> None:
    f = open(filename, 'w')
    
    f.write(sn)

def load_network(filename: str) -> dict:
    f = open(filename, 'r')
    
    new_net = f.read()
    f.close()
    
    return new_net