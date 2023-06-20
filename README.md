# ConstitutionUz
📜 Constitution of the Republic of Uzbekistan in python library.

<h1>Installing</h1>

You can install ConstitutionUz using pip:

<pre lang="bash">
pip install ConstitutionUz
</pre>


<h1>Usage</h1>

To use ConstitutionUz, first import the <code>ConstitutionUz</code> class from the <code>ConstitutionUz</code> package:

<pre lang="python">
# Import lib
from ConstitutionUz.ConstitutionUz import Constitution

const = Constitution("ru") # supports only ru, en and uz langs
print(const.search_constitution_by_keywords("мир"))
print(const.search_constitution_by_chapter(1))
</pre>


<h1>License</h1>
Library is licensed under the MIT License.
