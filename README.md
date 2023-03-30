# Content_based_Filtering_RecommendSystem

this project used Content_based filtering for recommendation system
libs referenced:
- underthesea:https://github.com/undertheseanlp/underthesea
- Gemmim: https://pypi.org/project/gensim/
- Cosine_similarity - Sklearn: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html

Data souce: Shopee ecommerce Platform
link: https://shopee.vn/Th%E1%BB%9Di-Trang-Nam-cat.11035567
Category: Thoi Trang Nam (Men Fashion)

there are 3 steps:
- 1. Preprocessing
- 2. Content_based_Gemmim
- 3. Content_based_Cosinesimilarity

the result shows as below:
- Product_based: a list of recommended items will be suggested to user when they are viewing a product
We assumed that user are viewing Item_ID: 23288601
And there will be 5 suggested items in recommendation (included similarity score)
  + Gemmim:
 Recommend 5 products similar to SÉT ĐỒ THỂ THAO NAM🚗 MẪU MONTER ĐỘC ĐÁO HÀNG BAO ĐẸP. FREEship....result below
-----
23317401
recommended product id:23317401, Sét Bộ Quần Áo Thể Thao Kẻ Sọc Cực Chất Cao Cấp, Áo Thun Cổ Tròn Ngắn Tay (score: )0.5098354)
16226602
recommended product id:16226602, [Có sẵn] Bộ Hè (score: )0.59065086)
23463701
recommended product id:23463701, Bộ thể thao nam hè NY phối nâu, Bộ nam thể thao hè NY thun lạnh không xù form dáng trẻ trung(score: )0.6075898)
1663702
recommended product id:1663702, BỘ thể thao nam nữ mẫu thun lạnh ETRENITEST mã ET(score: )0.91875774)
23322101
recommended product id:23322101, Nguyên bộ thể thao nam mẫu mới phong cách hàn quốc,🚛FREE SHIP🚛,(score: )0.99999994)
