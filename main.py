from boarding_passes.boarding_pass import BoardingPass
from boarding_sorter.sorter import sort_boarding_passes


def main():
    passes = [
        BoardingPass(transport_type="Train", origin="Madrid", destination="Barcelona", seat_assignment="45B"),
        BoardingPass(transport_type="Bus", origin="Barcelona", destination="Gerona Airport"),
        BoardingPass(transport_type="Flight", origin="Gerona Airport", destination="Stockholm", gate="45B", seat_assignment="3A"),
        BoardingPass(transport_type="Flight", origin="Stockholm", destination="New York JFK", gate="22", seat_assignment="7B"),
    ]
    sorted_passes = sort_boarding_passes(passes)

    for i, pass_ in enumerate(sorted_passes, start=1):
        print(f"{i}. {pass_}")
    print("You have arrived at your final destination.")


if __name__ == "__main__":
    main()
