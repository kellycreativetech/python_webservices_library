
import sugarcrm
#import sugarmodule

S = sugarcrm.Sugarcrm("http://ruttanvm.cs.kent.edu:4080/akubera/service/v2/rest.php", "admin", "admin")

a = S.get_module_fields('Accounts')

accounts = sugarcrm.Sugarmodule(S, 'Accounts')

retail = accounts.get_entries_where('accounts.industry = "retail"')
print accounts.prev_get_entries['next_offset']
raw_input()
retail =  accounts.get_next()
print accounts.prev_get_entries['next_offset']

retail =  accounts.get_next()
print accounts.prev_get_entries['next_offset']

retail =  accounts.get_next()
print accounts.prev_get_entries['next_offset']
	
exit()

industry = raw_input("Input Industry Name: ")

retail = accounts.get_entries_where("accounts.industry = '"+industry+"'")
list = ['d26b6c07-8f18-0f15-326e-4d41e0b4c29d','478e8eb3-4362-d662-df48-4d41e0c5035d','191f6b4a-0937-90d6-3d15-4d41e04decf4']
l = accounts.get_entries(list)

for i in l:
	print "\t",i.module,i.name,i.id
	
#print retail

#print type(a)

