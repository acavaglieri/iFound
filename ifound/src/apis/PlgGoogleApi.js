import axios from "axios";

export default {
  name: "googleApi",
  methods: {
    async sliceAddress(full_address) {
      let response = null;
      const payload = {
        full_address: full_address,
      };
      const path = `${process.env.VUE_APP_API_URL}/google_service/slice_address`;
      try {
        response = await axios.post(path, payload);
      } catch (error) {
        console.log(error)
      }
      return response;
    },
  },
};
