import ubidots


ubidots_client = ubidots.ApiClient(token='BBFF-Op6tcv8pCmOOZiQdDdVqqlD9mETC2n')
flagged_vehicles = ubidots_client.get_variable('6077ae071d84722afd9b1922')


def report(vehicle):
    flagged_vehicles.save_value({'value': vehicle.id})
