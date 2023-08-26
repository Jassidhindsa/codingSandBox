

def maximizeProfitOfSalesman(n, offers):
    offers_kept = []
    offers.sort(key = lambda x: (x[0], x[1]))
    # sorted(offers, key = lambda x : (x[:1]))
    print(offers)
    for offer in offers:
        if not offers_kept:
            print("ding", offer)
            offers_kept.append(offer)
        else:
            print(offers_kept, offer)
            last_offer = offers_kept[-1]
            first_house = last_offer[0]
            last_house = last_offer[1]
            last_offer_price = last_offer[2]
            last_offer_price_per_house = last_offer_price // (last_house  - first_house + 1)
            print(last_house, offer[0], last_offer_price_per_house)
            if last_house >= offer[0]:
                print("fish")
                this_house_offer_price_per_house = offer[2] // (offer[1] - offer[0] + 1)
                print(last_offer_price_per_house, this_house_offer_price_per_house)
                if this_house_offer_price_per_house > last_offer_price_per_house:
                    print("here ", offer, offers_kept)
                    offers_kept = offers_kept[:-1]
                    offers_kept.append(offer)
            else:
                offers_kept.append(offer)
    
    print(offers_kept)
    total_offer_price = 0
    for offer in offers_kept:
        total_offer_price += offer[2]
    
    return total_offer_price



if __name__ == "__main__":
    print(maximizeProfitOfSalesman(5, [[0,0,5],[3,3,1],[1,2,5],[0,0,7]]))