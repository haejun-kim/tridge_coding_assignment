# Dataset
1. How would you normalize (parsing, pre-processing, grouping) this data to simplify it’s processing into a database ?
   - 주어진 데이터를 확인했을 때, `Variety`, 'Grade', 'Region'에 대해 중복된 데이터가 존재한다는 것을 알 수 있다. 
   - 또한 각각의 데이터는 `Product`와 N:M 관계를 가지므로 이를 관계형 테이블로 분리해서 연결시키는 작업이 중복된 데이터를 효율적으로 저장할 수 있다.


2. What additional value can you extract from this dataset ? If you find any please explain how would you collect it (pseudo-algorithm)
   - 주어진 데이터를 통해서 어떤 나라의 어떤 지역에서 생산되는 어떤 품목의 가격 추이를 확인할 수 있다.
   - 가격 추이는 해당 상품의 가격이 가장 비싼 시기와 가격이 가장 저렴한 시기를 예측해 볼 수 있다.
   - 또한 수확이 되는 시기와 수확이 전혀 되지 않는 시기를 구분지을 수 있다.
     - 이러한 데이터는 Null값인 데이터가 몇달 지속되고 비슷한 시기에 다음 해에도 Null값이 지속된다면 Null값이 아닌 시기가 수확 시기라는 것을 확인할 수 있다.
   - 다른 가치로는 등급에 따른 가격 차이를 확인할 수 있다.


3. How would you approach the script of putting this information into a database ?(Concurrency, Scale, Prerequisites, etc..)
   - 이 부분은 잘 모르겠습니다.
