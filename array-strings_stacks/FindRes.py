class Solution:
    def filterRestaurants(self, restaurants: [[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> [int]:
        #list att in-order: [id, rating, veganFriendly, price, distance]
        #                   0       1       2              3    4
        
        #query out the items that match the provided criteria
        if veganFriendly == 1:
            restaurants = [x for x in restaurants if x[2] == 1 and x[3] <= maxPrice and x[4] <= maxDistance]
        else:
            restaurants = [x for x in restaurants if x[3] <= maxPrice and x[4] <= maxDistance]
            
        print(restaurants)
        
        # sort the restaurants by thier id from high to low. This is the key to getting the same rated restaurants id high to low
        restaurants.sort(key = lambda x: x[0], reverse = True) 
        
        print(restaurants)
        
        return [x[0] for x in sorted(restaurants, key=lambda y: y[1], reverse =True)] #return items by their ratings