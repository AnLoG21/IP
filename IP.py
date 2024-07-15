from openapi_client import openapi

token = 't.mr7EnMzoqBDvFHHvWetM9ZU_eqEa1L-3jhzFB1RAouRwEdgPh0M58QAFyQ6H5ywTkJ4go_FYxj9mwBpXduENUw'
client = openapi.api_client(token)
pf = client.portfolio.portfolio_get()
print('value:', pf.payload.positions[0].average_position_price.value)
print('currency:', pf.payload.positions[0].average_position_price.currency)
print('balance:', pf.payload.positions[0].balance)
print('figi:', pf.payload.positions[0].figi)
print('ticker:', pf.payload.positions[0].ticker)
print('name:', pf.payload.positions[0].name)
