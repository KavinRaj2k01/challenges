<template>
     <div>
        <h4 class="classname"> Question No :{{quizNo}} </h4>
        <p> Answer {{quizAnswer}}</p>
        <p> {{quizContent}}</p>
     <div class="answer-container">
        <!--<button class="answer-button" :class='{"correct-answer": x==quizAnswer, "wrong-answer":(userClickedAnswer != quizAnswer)&&userClickedAnswer==x}'  v-for="x in quizOptions" :key="x" disabled >{{x}}</button>-->
        <button class="next-button"> Next </button></div>
        <ButtonGroup :options="options"  :class='{"correct-answer": options==quizAnswer, "wrong-answer":(userClickedAnswer != quizAnswer)&&userClickedAnswer==options}' />
    </div>
</template>
<script>
import ButtonGroup from "../../components/ButtonGroup"
    export default{
     name:"AnswerPanel",
     props:["quizNo","quizContent","quizOptions","quizAnswer","userClickedAnswer","result"],
     components:{
      ButtonGroup
    },
data:function(){
      let options=[];
      for(let i=0;i<this.quizOptions.length;i++)
      {
        const option={label:this.quizOptions[i],value:this.quizOptions[i], disabled:false};
        options.push(option);
      }
      console.log(options);
      return {options:options}
    }

    }
</script>
<style scoped>
     .classname
     {
         color:blue;
     }
     .correct-answer
     {
         background-color: green;
     }
     .wrong-answer
     {
         background-color: red;
     }
     .next-button
     {
         align-self: flex-end;
           width:200px;
         height:50px;
  margin:10px;
  margin-right: 20%;
  border-radius:10px;
     }
</style>