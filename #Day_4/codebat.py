def front_back(str):
  len_str = len(str)
  if len_str <= 1:
    return str
  else:
    return str[len_str-1]+str[1:len_str-1]+str[0]

def front3(str):
  #ln = len(str)
  #if ln < 3:
  #  return str
  #else:
  return 3*str[:3]





###############################################################################
def string_times(str, n):
  return n*str

def front_times(str, n):
  return n*str[:3]


def string_bits(str):
    #1.############
    new_str = ''
    len_str = len(str)
    i = 0
    while len_str > 0:
      new_str = new_str+str[i]
      i+=2
      len_str -=2
    return new_str

    #2.#############
    new_str = ''
    len_str = len(str)
    for i in range(0,len_str,2):
      new_str = new_str + str[i]
    return new_str

    #3.#############
    new_str = ''
    len_str = len(str)
    for i in range(len_str):
        if i%2 == 0:
            new_str = new_str +str[i]
    return new_str


def string_splosion(str):
  new_str = ''
  for i in range(len(str)):
    new_str = new_str+str[0:i+1]
  return new_str



def last2(str):
  count = 0
  len_str = len(str)
  if len_str < 2:
    return 0
  else:
    for i in range(len_str-2):
      sub = str[i:i+2]
      if sub == str[-2:]:
        count +=1
  return count




