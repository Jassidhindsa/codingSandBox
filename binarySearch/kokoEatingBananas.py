
import math

def kokoEatingBananas(piles, hours):
    min_speed, max_speed = 1, max(piles)
    final_speed = max(piles)

    while min_speed <= max_speed:
        avg_speed = (min_speed + max_speed) // 2
        total_time_taken = 0

        for pile in piles:
            total_time_taken += int(pile / avg_speed)
        
        if total_time_taken <= hours:
            final_speed = min(final_speed, avg_speed)
            max_speed = avg_speed - 1
        else:
            min_speed = avg_speed + 1
    
    return final_speed


if __name__ == "__main__":
    print(kokoEatingBananas([3,6,7,11], 8))