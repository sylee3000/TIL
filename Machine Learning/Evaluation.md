# Evaluation (평가)

- 이진 분류에서의 성능 평가 지표
  - Accuracy, Confusion Matrix, Precision, Recall, F1 score, ROC / AUC

- 정확도
  - 예측 결과가 실제 값과 얼마나 동일한지를 나타내는 평가 지표
  - 불균형한 분포를 가지는 데이터에서는 좋은 평가 지표가 되지 못함

- 오차 행렬 : 이진 분류에서 예측 오류들이 얼마나 발생하는지를 나타내는 행렬
  - True Negative (Negative를 Negative로 제대로 예측)
  - False Negative (Negative를 Positive로 잘못 예측)
  - True Positive (Positive를 Positive로 제대로 예측)
  - False Positive (Positive를 Negative로 잘못 예측)

- 정밀도와 재현율
  - 정밀도 : Positive로 예측한 대상 중에서 실제로 Positive인 데이터의 비율, 가급적 Negative라고 예측하는 것이 나은 경우에 중요하다.
  - 재현율 : 실제로 Positive인 데이터 중에서 예상을 Positive로 한 비율, 가급적 Positive라고 예측하는 것이 나은 경우에 중요하다.
  - 정밀도/재현율 트레이드오프 : 둘 중 하나를 높이면 다른 하나의 수치가 떨어짐

- F1 score
  - 정밀도와 재현율을 결합. 두 수치가 차이가 없을 수록 더 좋은 F1 score를 가지게 된다.

- ROC / AUC
  - ROC 곡선 : FPR에 따른 TPR의 변화를 나타내는 곡선이다. ROC 곡선의 밑부분의 면적을 AUC 값이라고 한다.
  - FPR : 실제 Negative인 데이터를 Positive로 잘못 예측한 비율, TPR : 재현율
