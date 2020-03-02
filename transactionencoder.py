
def transaction_encoder(df):
	'''
	input: dataframe, transaction table,
			where each row is a transaction of items
	output: columns are distinct items, values 1 or 0
	'''

	# Make df a list of list of items
	df_list = df.values.tolist()

	# Put all items in a list
	all_items = []
	for transaction in df_list:
	    for item in transaction:
	        if str(item) != 'nan':
	            all_items.append(item)

	# Get distinct items
	list_items = list(set(all_items))

	item_encoded = []
	for transaction in df_list:
	    transaction_list = []
	    for item in list_items:
	        if item in transaction:
	            transaction_list.append(1)
	        else:
	            transaction_list.append(0)
	    item_encoded.append(transaction_list)

	return pd.DataFrame(item_encoded, columns=list_items)