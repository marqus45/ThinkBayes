"""
Chapter 2 computional statisitics
"""

from code3.thinkbayes import Pmf

pmf = Pmf()
for x in range(1, 7):
    pmf.Set(x, 1 / 6.0)

word_list = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin faucibus, massa vitae vulputate ultricies, nulla ipsum pulvinar leo, et sollicitudin lacus metus non neque. Suspendisse vulputate mauris purus, eget elementum sem hendrerit vitae. Morbi ornare viverra cursus. Fusce nec vulputate lacus, a tincidunt urna. Donec eu finibus urna. Donec cursus vehicula velit, vel convallis mauris vehicula at. Sed vitae imperdiet urna, id rutrum est. Vestibulum a nulla quis ante luctus ornare quis sed magna. Morbi pharetra vehicula velit, at sollicitudin nisi malesuada et.
Nulla facilisi. Curabitur quis efficitur augue. Integer iaculis porta mattis. Sed blandit ultricies dolor a mollis. Fusce porttitor libero enim, at dignissim arcu sollicitudin vitae. Phasellus tristique cursus metus. Vivamus commodo pellentesque ultricies. Mauris facilisis egestas vehicula.
In a nisl non orci laoreet interdum. Donec malesuada mi eu metus dictum, in rutrum urna consectetur. Proin rhoncus enim molestie dui cursus finibus. Nullam accumsan lectus in diam faucibus, vitae malesuada ligula cursus. Nulla sed semper elit. Nullam faucibus, felis sit amet elementum malesuada, massa sapien rutrum lectus, nec ultrices nulla odio a orci. Vestibulum finibus, augue faucibus sollicitudin tincidunt, urna est laoreet erat, ut semper arcu purus a quam. Mauris turpis nunc, tincidunt eget fringilla vel, molestie vel diam. In hac habitasse platea dictumst. Etiam nec porttitor arcu. Aenean porttitor dolor et rhoncus iaculis. Mauris porta volutpat purus, et elementum ligula auctor non. Proin posuere, sapien lobortis vestibulum malesuada, nibh risus fermentum nibh, vitae convallis lorem nisl ac elit. Nunc ac enim id est porta imperdiet et id nunc. Nullam viverra urna pellentesque nibh bibendum laoreet et quis quam. Donec hendrerit nec massa eget pulvinar.
Quisque euismod libero id magna bibendum, ac ultrices justo euismod. Fusce id massa ac urna semper malesuada quis ut diam. Nunc eu fringilla sem. Aenean vitae nisl tristique, auctor orci sed, porta lectus. Curabitur sollicitudin elementum elit, at faucibus ipsum hendrerit eu. Sed non consectetur dolor, et scelerisque erat. Vestibulum dapibus, odio vel dictum fringilla, turpis felis porta justo, quis viverra arcu diam facilisis ex. Integer cursus dignissim lacus vel iaculis. Ut sit amet fermentum dui, sit amet dictum purus. Sed dictum in lorem eu ultrices. Vivamus eget ornare dolor. Proin eu nisl vitae ex bibendum ultrices at sed lectus. Aliquam congue semper euismod. In hac habitasse platea dictumst. Nunc placerat elit sit amet velit imperdiet bibendum.
Phasellus aliquet ullamcorper interdum. Proin non lorem turpis. Vivamus sodales magna sed enim blandit porttitor. Proin eu sem lectus. Ut eget ante eu odio pharetra consectetur. Duis efficitur cursus augue, vitae finibus massa mattis eu. Cras sagittis tincidunt enim dictum iaculis. Suspendisse imperdiet id diam sed placerat. Sed sed libero luctus, imperdiet dolor a, sodales urna. Morbi ac tellus venenatis, placerat nibh a, tristique justo. Cras leo lacus, vulputate et vestibulum at, fermentum vitae enim. Integer convallis laoreet sapien, ut vehicula augue vulputate sit amet. Proin condimentum sapien eget faucibus eleifend.
Aliquam eu ligula ac erat facilisis consectetur. Integer quis ligula quam. Maecenas mollis auctor dolor, nec volutpat lacus luctus tincidunt. Cras tincidunt vulputate mi quis. """.split()


pmf_wrd = Pmf()
for wrd in word_list:
    pmf.Incr(wrd, 1)
pmf_wrd.Normalize()

print(pmf.Prob(6))
print()
print(pmf_wrd.Prob('sit'))