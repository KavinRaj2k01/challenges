<template>
  <div>
    <Header title="Quiz-App4" />
    <StartPanel :onclickStart="onClickStart" v-if="state.panel === 'Start'" />
    <QuizPanel
      v-if="state.panel === 'Quiz'"
      :quizNo="quizzes.quizzes[state.currentQuizIndex].quizNo"
      :quizContent="quizzes.quizzes[state.currentQuizIndex].quizContent"
      :quizOptions="quizzes.quizzes[state.currentQuizIndex].quizOptions"
      :quizAnswer="quizzes.quizzes[state.currentQuizIndex].quizAnswer"
      :onQuizAnswer="onQuizAnswer"
    />
    <AnswerPanel v-if="state.panel === 'Answer'" 
      :quizNo="quizzes.quizzes[state.currentQuizIndex].quizNo"
      :quizContent="quizzes.quizzes[state.currentQuizIndex].quizContent"
      :quizOptions="quizzes.quizzes[state.currentQuizIndex].quizOptions"
      :quizAnswer="quizzes.quizzes[state.currentQuizIndex].quizAnswer"
      :userClickedAnswer="userClickedAnswer"/>
  </div>
</template>
<script>
import Header from "../components/Header";
//import StartPanel from "./panels/StartPanel"
import QuizPanel from "./panels/QuizPanel";
import StartPanel from "./panels/StartPanel.vue";
import AnswerPanel from "./panels/AnswerPanel";
import quizzes from "../sources/quizzes.json"
const screens = { start: "Start", quiz: "Quiz",answer:"Answer" };

console.log(JSON.stringify(quizzes));


export default {
  name: "MainScreen",
  props: ["userName"],
  components: {
    Header,
    StartPanel,
    QuizPanel,
    AnswerPanel
  },
  data: function () {
    return {
    state: { panel: screens.start, currentQuizIndex:0 } ,
    userClickedAnswer:"",
    quizzes:quizzes};
  },
  //{ state : {panel: screens.start}}
  methods: {
    onClickStart: function () {
      this.state.panel = screens.quiz;
    },
    onQuizAnswer: function (result,userClickedAnswer) {
         console.log(`Result is ${result}. ${userClickedAnswer}`);
         this.state.panel = screens.answer;
         this.userClickedAnswer=userClickedAnswer;
    },
  },
};
</script>
