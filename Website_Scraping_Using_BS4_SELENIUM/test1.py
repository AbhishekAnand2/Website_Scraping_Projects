
text = "//cdn.shopify.com/s/files/1/0018/4441/2493/products/CBDMixedBerry-1_200x.png?v=1594835986 200w, //cdn.shopify.com/s/files/1/0018/4441/2493/products/CBDMixedBerry-1_400x.png?v=1594835986 400w, //cdn.shopify.com/s/files/1/0018/4441/2493/products/CBDMixedBerry-1_600x.png?v=1594835986 600w, //cdn.shopify.com/s/files/1/0018/4441/2493/products/CBDMixedBerry-1_700x.png?v=1594835986 700w, //cdn.shopify.com/s/files/1/0018/4441/2493/products/CBDMixedBerry-1_800x.png?v=1594835986 800w, //cdn.shopify.com/s/files/1/0018/4441/2493/products/CBDMixedBerry-1_900x.png?v=1594835986 900w, //cdn.shopify.com/s/files/1/0018/4441/2493/products/CBDMixedBerry-1_1000x.png?v=1594835986 1000w, //cdn.shopify.com/s/files/1/0018/4441/2493/products/CBDMixedBerry-1_1200x.png?v=1594835986 1200w, //cdn.shopify.com/s/files/1/0018/4441/2493/products/CBDMixedBerry-1_1400x.png?v=1594835986 1400w, //cdn.shopify.com/s/files/1/0018/4441/2493/products/CBDMixedBerry-1_1600x.png?v=1594835986 1600w"


# print(text.find("800w"))
# print(text.find("900w"))
print(text[text.find("800w")+6:text.find("900w")])