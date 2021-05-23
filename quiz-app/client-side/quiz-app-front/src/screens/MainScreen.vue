<template>
  <div>
    <Header title="Quiz-App4" />
    <StartPanel :onclickStart="onClickStart" v-if="state.panel === 'Start'" />
    <QuizPanel
      v-if="state.panel === 'Quiz'"
      quizNo="1"
      quizContent="Number of sides does Square have"
      :quizOptions="['1', '2', '3', '4']"
      quizAnswer="4"
      :onQuizAnswer="onQuizAnswer"
    />
    <AnswerPanel v-if="state.panel === 'Answer'"   quizNo="1"
      quizContent="Number of sides does Square have"
      :quizOptions="['1', '2', '3', '4']"
      quizAnswer="4"/>
  </div>
</template>
<script>
import Header from "../components/Header";
//import StartPanel from "./panels/StartPanel"
import QuizPanel from "./panels/QuizPanel";
import StartPanel from "./panels/StartPanel.vue";
import AnswerPanel from "./panels/AnswerPanel";
const screens = { start: "Start", quiz: "Quiz",answer:"Answer" };
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
    return { state: { panel: screens.start } };
  },
  //{ state : {panel: screens.start}}
  methods: {
    onClickStart: function () {
      this.state.panel = screens.quiz;
    },
    onQuizAnswer: function (result,userClickedAnswer) {
         console.log(`Result is ${result}. ${userClickedAnswer}`);
         this.state.panel = screens.answer;
    },
  },
};
</script>
