<!--<script>
import { Doughnut } from "vue-chartjs";

export default {
  extends: Doughnut,
  props: {
    ins: {
      type: Number,
      required: true,
    },
    outs: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      insPercent: null,
      outsPercent: null,
      datacollection: {
        labels: ["Entradas", "Saídas"],
        datasets: [
          {
            data: [0, 0],
            backgroundColor: ["#71c016", "#ffc100", "#248afd"],
            borderColor: "rgba(0,0,0,0)",
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: true,
        segmentShowStroke: false,
        cutoutPercentage: 75,
        elements: {
          arc: {
            borderWidth: 4,
          },
        },
        legend: {
          display: false,
        },
        tooltips: {
          enabled: false,
        },
      },
      northAmericaChartPlugins: {
        beforeDraw: function (chart) {
          var width = chart.chart.width,
            height = chart.chart.height,
            ctx = chart.chart.ctx;

          ctx.restore();
          var fontSize = 3.125;
          ctx.font = "600 " + fontSize + "em sans-serif";
          ctx.textBaseline = "middle";
          ctx.fillStyle = "#000";

          var text = "90",
            textX = Math.round((width - ctx.measureText(text).width) / 2),
            textY = height / 2;

          ctx.fillText(text, textX, textY);
          ctx.save();
        },
      },
    };
  },
  methods: {
    async calcPercentage() {
      let hundredPercent = this.ins + this.outs;
      this.insPercent = (this.ins / hundredPercent) * 100;
      this.outsPercent = (this.outs / hundredPercent) * 100;
      this.datacollection.datasets[0].data = [
        this.insPercent,
        this.outsPercent,
      ];
      let emit = {
        outsPercent: this.outsPercent,
        insPercent: this.insPercent,
      };
      await this.$emit("totalPercentages", emit);
      await this.renderChart(this.datacollection, this.options);
    },
  },
  async mounted() {
    await this.calcPercentage();
  },
};
</script>
