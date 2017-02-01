def weird(user_name, **kwargs):
  first_name = kwargs["first_name"]
  last_name = kwargs["last_name"]
  return \
    user_name + "'s full name is " + \
    first_name + " " + last_name
    
print weird(
    "@gwashington",
    first_name="George",
    last_name="Washington"
    )