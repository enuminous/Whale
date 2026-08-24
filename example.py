from whale import WhaleEvaluator

history = [
    0.50,0.51,0.50,0.52,0.53,
    0.55,0.57,0.60,0.63,0.66,
    0.68,0.69,0.70,0.70,0.71
]

pre = [0.50,0.51,0.50]
post = [0.69,0.70,0.71]

print(WhaleEvaluator().evaluate(
    history,
    baseline=0.50,
    pre=pre,
    post=post
))
