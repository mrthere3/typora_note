# *VUE*学习记录

## 快速原型开发（单个vue文件调试）

1. ~~~vue
   npm install -g vue-cli@4.0
   ~~~
   
2. ~~~vue
   npm install -g @vue/cli-service-global
   ~~~

3. ~~~vue
   npm i -g eslint <!-- 防止vue文件调用js报错-->
   ~~~

4.  ~~~vue
    npm install vue-template-compiler 
    ~~~

5. 创建文件夹并创建单个vue组件 test.vue

6. ~~~vue
   npm init #生成page.json
   ~~~

7.  ~~~vue
    vue serve test.vue <!--快速调用开发者模式调用vue文件-->
    ~~~

8. 
  
     ![](https://cdn.jsdelivr.net/gh/mrthere3/typora_note/img/js/202209281213803.png)

# vue基础

## 类与样式绑定

### 绑定对象

数据绑定的一个常见需求场景是操纵元素的 CSS class 列表和内联样式。因为 class 和 style 都是 attribute，我们可以和其他 attribute 一样使用 v-bind 将它们和动态的字符串绑定。但是，在处理比较复杂的绑定时，通过拼接生成字符串是麻烦且易出错的。因此，Vue 专门为 class 和 style 的 v-bind 用法提供了特殊的功能增强。除了字符串外，表达式的值也可以是对象或数组。

我们可以给 `:class` (`v-bind:class` 的缩写) 传递一个对象来动态切换 class：

~~~vue
<div :class="{ active: isActive }"></div>
~~~

上面的语法表示 `active` 是否存在取决于数据属性 `isActive` 的真假。

### 绑定数组

我们可以给 `:class` 绑定一个数组来渲染多个 CSS class：

~~~js
data() {
  return {
    activeClass: 'active',
    errorClass: 'text-danger'
  }
}
<div :class="[activeClass, errorClass]"></div>
~~~

渲染的结果是

~~~vue
<div class="active text-danger"></div>
~~~

配合三元表达式 

~~~vue
<div :class="[isActive ? activeClass : '', errorClass]"></div>
~~~

## 绑定内联样式

:style 支持绑定 JavaScript 对象值，对应的是 HTML 元素的 style 属性：

~~~js
data() {
  return {
    activeColor: 'red',
    fontSize: 30
  }
}
<div :style="{ color: activeColor, fontSize: fontSize + 'px' }"></div>
~~~

尽管推荐使用 camelCase，但 `:style` 也支持 kebab-cased 形式的 CSS 属性 key (对应其 CSS 中的实际名称)，例如：

~~~vue
<div :style="{ 'font-size': fontSize + 'px' }"></div>
~~~

直接绑定一个样式对象通常是一个好主意，这样可以使模板更加简洁：

~~~js
data() {
  return {
    styleObject: {
      color: 'red',
      fontSize: '13px'
    }
  }
}
<div :style="styleObject"></div>
~~~

## 条件渲染

### `v-if`

`v-if` 指令用于条件性地渲染一块内容。这块内容只会在指令的表达式返回真值时才被渲染。

~~~vue
<h1 v-if="awesome">Vue is awesome!</h1>
~~~

### `v-else`

你也可以使用 `v-else` 为 `v-if` 添加一个“else 区块”。

~~~vue
<button @click="awesome = !awesome">Toggle</button>

<h1 v-if="awesome">Vue is awesome!</h1>
<h1 v-else>Oh no 😢</h1>
~~~

### `v-else-if`

顾名思义，v-else-if 提供的是相应于 v-if 的“else if 区块”。它可以连续多次重复使用：

~~~vue
<div v-if="type === 'A'">
  A
</div>
<div v-else-if="type === 'B'">
  B
</div>
<div v-else-if="type === 'C'">
  C
</div>
<div v-else>
  Not A/B/C
</div>
~~~

和 v-else 类似，一个使用 v-else-if 的元素必须紧跟在一个 v-if 或一个 v-else-if 元素后面。

### `<template>` 上的 `v-if`

因为 `v-if` 是一个指令，他必须依附于某个元素。但如果我们想要切换不止一个元素呢？在这种情况下我们可以在一个 `<template>` 元素上使用 `v-if`，这只是一个不可见的包装器元素，最后渲染的结果并不会包含这个 `<template>` 元素。

~~~vue
<template v-if="ok">
  <h1>Title</h1>
  <p>Paragraph 1</p>
  <p>Paragraph 2</p>
</template>
~~~

### `v-show`

另一个可以用来按条件显示一个元素的指令是 v-show。其用法基本一样：

~~~vue
<h1 v-show="ok">Hello!</h1>
~~~

不同之处在于 v-show 会在 DOM 渲染中保留该元素；v-show 仅切换了该元素上名为 display 的 CSS 属性。

v-show 不支持在 <template> 元素上使用，也不能和 v-else 搭配使用。

## 列表渲染

### `v-for`

我们可以使用 v-for 指令基于一个数组来渲染一个列表。v-for 指令的值需要使用 item in items 形式的特殊语法，其中 items 是源数据的数组，而 item 是迭代项的别名：

~~~vue
data() {
  return {
    items: [{ message: 'Foo' }, { message: 'Bar' }]
  }
}
<li v-for="item in items">
  {{ item.message }}
</li>
~~~

在 v-for 块中可以完整地访问父作用域内的属性和变量。v-for 也支持使用可选的第二个参数表示当前项的位置索引。

~~~js
data() {
  return {
    parentMessage: 'Parent',
    items: [{ message: 'Foo' }, { message: 'Bar' }]
  }
}
~~~

~~~vue
<li v-for="(item, index) in items">
  {{ parentMessage }} - {{ index }} - {{ item.message }}
</li>
~~~

对于多层嵌套的 v-for，作用域的工作方式和函数的作用域很类似。每个 v-for 作用域都可以访问到父级作用域：

~~~vue
<li v-for="item in items">
  <span v-for="childItem in item.children">
    {{ item.message }} {{ childItem }}
  </span>
</li>
~~~

你也可以使用 of 作为分隔符来替代 in，这更接近 JavaScript 的迭代器语法：

~~~vue
<div v-for="item of items"></div>
~~~

### `v-for` 与对象

你也可以使用 `v-for` 来遍历一个对象的所有属性。遍历的顺序会基于对该对象调用 `Object.keys()` 的返回值来决定。

~~~vue
data() {
  return {
    myObject: {
      title: 'How to do lists in Vue',
      author: 'Jane Doe',
      publishedAt: '2016-04-10'
    }
  }
}
<ul>
  <li v-for="value in myObject">
    {{ value }} <!--value表示属性值--> 
  </li>
</ul>
~~~

可以通过提供第二个参数表示属性名 (例如 key)：

~~~vue
<li v-for="(value, key) in myObject">
  {{ key }}: {{ value }}
</li>
~~~

第三个参数表示位置索引：

~~~vue
<li v-for="(value, key, index) in myObject">
  {{ index }}. {{ key }}: {{ value }}
</li>

~~~

### 在 `v-for` 里使用范围值

v-for 可以直接接受一个整数值。在这种用例中，会将该模板基于 1...n 的取值范围重复多次。

~~~vue
<span v-for="n in 10">{{ n }}</span>
~~~

注意此处 n 的初值是从 1 开始而非 0。

### `<template>` 上的 `v-for`

与模板上的 `v-if` 类似，你也可以在 `<template>` 标签上使用 `v-for` 来渲染一个包含多个元素的块。例如：

~~~vue
<ul>
  <template v-for="item in items">
    <li>{{ item.msg }}</li>
    <li class="divider" role="presentation"></li>
  </template>
</ul>

~~~

### `v-for` 与 `v-if`

当它们同时存在于一个节点上时，`v-if` 比 `v-for` 的优先级更高。这意味着 `v-if` 的条件将无法访问到 `v-for` 作用域内定义的变量别名：

~~~vue
<!--
 这会抛出一个错误，因为属性 todo 此时
 没有在该实例上定义
-->
<li v-for="todo in todos" v-if="!todo.isComplete">
  {{ todo.name }}
</li>
<!--
 这会抛出一个错误，因为属性 todo 此时
 没有在该实例上定义
-->
<li v-for="todo in todos" v-if="!todo.isComplete">
  {{ todo.name }}
</li>
~~~

## 事件处理`v-on`

### 监听事件`v-on`

我们可以使用 `v-on` 指令 (简写为 `@`) 来监听 DOM 事件，并在事件触发时执行对应的 JavaScript。用法：`v-on:click="methodName"` 或 `@click="handler"`。

事件处理器的值可以是：

1. **内联事件处理器**：事件被触发时执行的内联 JavaScript 语句 (与 `onclick` 类似)。

2. **方法事件处理器**：一个指向组件上定义的方法的属性名或是路径。     

   ****

### 内联事件处理器

内联事件处理器通常用于简单场景，例如：

~~~vue
data() {
  return {
    count: 0
  }
}
<button @click="count++">Add 1</button>
<p>Count is: {{ count }}</p>
~~~

****

### 方法事件处理器

随着事件处理器的逻辑变得愈发复杂，内联代码方式变得不够灵活。因此 v-on 也可以接受一个方法名或对某个方法的调用。

~~~vue
data() {
  return {
    name: 'Vue.js'
  }
},
methods: {
  greet(event) {
    // 方法中的 `this` 指向当前活跃的组件实例
    alert(`Hello ${this.name}!`)
    // `event` 是 DOM 原生事件
    if (event) {
      alert(event.target.tagName)
    }
  }
}
<!-- `greet` 是上面定义过的方法名 -->
<button @click="greet">Greet</button>

~~~



### 方法与内联事件判断

模板编译器会通过检查 v-on 的值是否是合法的 JavaScript 标识符或属性访问路径来断定是何种形式的事件处理器。举例来说，foo、foo.bar 和 foo['bar'] 会被视为方法事件处理器，而 foo() 和 count++ 会被视为内联事件处理器



### 在内联处理器中调用方法

除了直接绑定方法名，你还可以在内联事件处理器中调用方法。这允许我们向方法传入自定义参数以代替原生事件：

~~~vue
methods: {
  say(message) {
    alert(message)
  }
}
<button @click="say('hello')">Say hello</button>
<button @click="say('bye')">Say bye</button>
~~~

****



### 在内联事件处理器中访问事件参数

有时我们需要在内联事件处理器中访问原生 DOM 事件。你可以向该处理器方法传入一个特殊的 `$event` 变量，或者使用内联箭头函数：

~~~vue
<!-- 使用特殊的 $event 变量 -->
<button @click="warn('Form cannot be submitted yet.', $event)">
  Submit
</button>

<!-- 使用内联箭头函数 -->
<button @click="(event) => warn('Form cannot be submitted yet.', event)">
  Submit
</button>
methods: {
  warn(message, event) {
    // 这里可以访问 DOM 原生事件
    if (event) {
      event.preventDefault()
    }
    alert(message)
  }
}

~~~

****



### 事件修饰符

在处理事件时调用 `event.preventDefault()` 或 `event.stopPropagation()` 是很常见的。尽管我们可以直接在方法内调用，但如果方法能更专注于数据逻辑而不用去处理 DOM 事件的细节会更好。

为解决这一问题，Vue 为 `v-on` 提供了**事件修饰符**。修饰符是用 `.` 表示的指令后缀，包含以下这些：

- `.stop`

- `.prevent`

- `.self`

- `.capture`

- `.once`

- `.passive`

  

~~~vue
<!-- 单击事件将停止传递 -->
<a @click.stop="doThis"></a>

<!-- 提交事件将不再重新加载页面 -->
<form @submit.prevent="onSubmit"></form>

<!-- 修饰语可以使用链式书写 -->
<a @click.stop.prevent="doThat"></a>

<!-- 也可以只有修饰符 -->
<form @submit.prevent></form>

<!-- 仅当 event.target 是元素本身时才会触发事件处理器 -->
<!-- 例如：事件处理器不来自子元素 -->
<div @click.self="doThat">...</div>

~~~

****



### 按键修饰符

在监听键盘事件时，我们经常需要检查特定的按键。Vue 允许在 `v-on` 或 `@` 监听按键事件时添加按键修饰符。

~~~vue
<!-- 仅在 `key` 为 `Enter` 时调用 `submit` -->
<input @keyup.enter="submit" />
~~~

你可以直接使用 [`KeyboardEvent.key`](https://developer.mozilla.org/zh-CN/docs/Web/API/KeyboardEvent/key/Key_Values) 暴露的按键名称作为修饰符，但需要转为 kebab-case 形式。

~~~vue
<input @keyup.page-down="onPageDown" />
~~~

在上面的例子中，仅会在 `$event.key` 为 `'PageDown'` 时调用事件处理。

### 按键别名

Vue 为一些常用的按键提供了别名：

- `.enter`
- `.tab`
- `.delete` (捕获“Delete”和“Backspace”两个按键)
- `.esc`
- `.space`
- `.up`
- `.down`
- `.left`
- `.right`

### 系统按键修饰符

你可以使用以下系统按键修饰符来触发鼠标或键盘事件监听器，只有当按键被按下时才会触发。

- `.ctrl`
- `.alt`
- `.shift`
- `.meta`

注意

在 Mac 键盘上，meta 是 Command 键 (⌘)。在 Windows 键盘上，meta 键是 Windows 键 (⊞)。在 Sun 微机系统键盘上，meta 是钻石键 (◆)。在某些键盘上，特别是 MIT 和 Lisp 机器的键盘及其后代版本的键盘，如 Knight 键盘，space-cadet 键盘，meta 都被标记为“META”。在 Symbolics 键盘上，meta 也被标识为“META”或“Meta”。

### `.exact` 修饰符

`.exact` 修饰符允许控制触发一个事件所需的确定组合的系统按键修饰符。

~~~vue
<!-- 当按下 Ctrl 时，即使同时按下 Alt 或 Shift 也会触发 -->
<button @click.ctrl="onClick">A</button>

<!-- 仅当按下 Ctrl 且未按任何其他键时才会触发 -->
<button @click.ctrl.exact="onCtrlClick">A</button>

<!-- 仅当没有按下任何系统按键时触发 -->
<button @click.exact="onClick">A</button>

~~~

****

### 鼠标按键修饰符

- `.left`
- `.right`
- `.middle`

这些修饰符将处理程序限定为由特定鼠标按键触发的事件。

## 表单输入绑定

在前端处理表单时，我们常常需要将表单输入框的内容同步给 JavaScript 中相应的变量。手动连接值绑定和更改事件监听器可能会很麻烦：

~~~vue
<input
  :value="text"
  @input="event => text = event.target.value">

~~~

`v-model` 指令帮我们简化了这一步骤：

~~~vue
<input v-model="text">

~~~

另外，`v-model` 还可以用于各种不同类型的输入，`<textarea>`、`<select>` 元素。它会根据所使用的元素自动使用对应的 DOM 属性和事件组合：

- 文本类型的 `<input>` 和 `<textarea>` 元素会绑定 `value` property 并侦听 `input` 事件；
- `<input type="checkbox">` 和 `<input type="radio">` 会绑定 `checked` property 并侦听 `change` 事件；
- `<select>` 会绑定 `value` property 并侦听 `change` 事件

### 基本用法

#### 文本

~~~vue
<p>Message is: {{ message }}</p>
<input v-model="message" placeholder="edit me" />

~~~

#### 多行文本

~~~vue
<span>Multiline message is:</span>
<p style="white-space: pre-line;">{{ message }}</p>
<textarea v-model="message" placeholder="add multiple lines"></textarea>

~~~

注意在 `<textarea>` 中是不支持插值表达式的。请使用 `v-model` 来替代：

~~~vue
<!-- 错误 -->
<textarea>{{ text }}</textarea>

<!-- 正确 -->
<textarea v-model="text"></textarea>

~~~



#### 复选框

单一的复选框，绑定布尔类型值：

~~~vue
<input type="checkbox" id="checkbox" v-model="checked" />
<label for="checkbox">{{ checked }}</label>

~~~

我们也可以将多个复选框绑定到同一个数组或集合的值：

~~~vue
export default {
  data() {
    return {
      checkedNames: []
    }
  }
}
<div>Checked names: {{ checkedNames }}</div>

<input type="checkbox" id="jack" value="Jack" v-model="checkedNames">
<label for="jack">Jack</label>

<input type="checkbox" id="john" value="John" v-model="checkedNames">
<label for="john">John</label>

<input type="checkbox" id="mike" value="Mike" v-model="checkedNames">
<label for="mike">Mike</label>

~~~

#### 单选按钮

~~~vue
<div>Picked: {{ picked }}</div>

<input type="radio" id="one" value="One" v-model="picked" />
<label for="one">One</label>

<input type="radio" id="two" value="Two" v-model="picked" />
<label for="two">Two</label>

~~~

#### 选择器

单个选择器的示例如下：

~~~vue
<div>Selected: {{ selected }}</div>

<select v-model="selected">
  <option disabled value="">Please select one</option>
  <option>A</option>
  <option>B</option>
  <option>C</option>
</select>

~~~

多选 (值绑定到一个数组)：

~~~vue
<div>Selected: {{ selected }}</div>

<select v-model="selected" multiple>
  <option>A</option>
  <option>B</option>
  <option>C</option>
</select>
~~~

选择器的选项可以使用 `v-for` 动态渲染：

~~~vue
export default {
  data() {
    return {
      selected: 'A',
      options: [
        { text: 'One', value: 'A' },
        { text: 'Two', value: 'B' },
        { text: 'Three', value: 'C' }
      ]
    }
  }
}
<select v-model="selected">
  <option v-for="option in options" :value="option.value">
    {{ option.text }}
  </option>
</select>

<div>Selected: {{ selected }}</div>

~~~



#### 值绑定

对于单选按钮，复选框和选择器选项，`v-model` 绑定的值通常是静态的字符串 (或者对复选框是布尔值)：

~~~vue
<!-- `picked` 在被选择时是字符串 "a" -->
<input type="radio" v-model="picked" value="a" />

<!-- `toggle` 只会为 true 或 false -->
<input type="checkbox" v-model="toggle" />

<!-- `selected` 在第一项被选中时为字符串 "abc" -->
<select v-model="selected">
  <option value="abc">ABC</option>
</select>

~~~

但有时我们可能希望将该值绑定到当前组件实例上的动态数据。这可以通过使用 `v-bind` 来实现。此外，使用 `v-bind` 还使我们可以将选项值绑定为非字符串的数据类型。
