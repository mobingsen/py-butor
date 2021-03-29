# encoding=utf8
# pip install lxml
from lxml import etree

xml = """
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id="10086">周大强</nick>
        <nick id="10010">周芷若</nick>
        <nick class="joy">周杰伦</nick>
        <nick class="jolin">蔡依林</nick>
        <div>
            <nick>惹了</nick>
        </div>
    </author>
    <partner>
        <nick id="ppc">胖胖陈</nick>
        <nick id="ppbc">胖胖不陈</nick>
    </partner>
</book>
"""

tree = etree.XML(xml)
# result = tree.xpath("/book")
# result = tree.xpath("/book/name/text()") # 拿name标签中的文本
# result = tree.xpath("/book/author/nick/text()")
# result = tree.xpath("/book/author//nick/text()")
result = tree.xpath("/book/author/*/nick/text()")

print(result)
