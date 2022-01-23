# wordle
## Sample Use
```
>>> w=Wordle()
>>> w.update("Today", "bbbbb")
>>> w.get_choices()[:10]
['30-30', 'b.ch.', 'b.sc.', 'bcere', 'bebel', 'beche', 'becki', 'becks', 'beebe', 'beech']
>>> w.update("Becks", "bbybb")
>>> w.get_choices()[:10]
['chich', 'chili', 'chill', 'chimp', 'chimu', "ch'in", 'chin.', 'ching', 'chir-', 'chirl']
>>> w.update("Chimp", "gbggg")
>>> w.get_choices()
['crimp']
```


![example usage](https://pbs.twimg.com/media/FJx4-zgaQAA_5jL?format=jpg&name=large)
https://twitter.com/bhamshudhiman/status/1485195019153973248/photo/1
