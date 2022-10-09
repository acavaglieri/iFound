import { helpers } from 'vuelidate/lib/validators';
import validateCPF from './vuelidateCPF';
import validateCNPJ from './vuelidateCNPJ';

const customValidators = {};

customValidators.minCheck  = (min) => helpers.withParams(
	{ type: 'minCheck', min: min },
	(value) => !helpers.req(value) || value.length >= min
);
customValidators.maxCheck = (max) => helpers.withParams(
	{ type: 'maxCheck', max: max },
	(value) => !helpers.req(value) || value.length <= max
);
customValidators.minMaxCheck = (min, max) => helpers.withParams(
	{ type: 'minMaxCheck', min:min, max: max },
	(value) => !helpers.req(value) || (min <= value.length && value.length <= max)
);
customValidators.minMaxCheckNumberMask = (min, max) => helpers.withParams(
	{ type: 'minMaxCheckNumberMask', min:min, max: max },
	function (value) {
		value = value.replace(/\D/g, "");
		return !helpers.req(value) || (min <= value.length && value.length <= max);
	}
);
customValidators.cpfValidCheck = () => helpers.withParams(
	{ type: 'cpfValidCheck' },
	function (value) {
		if(!value) {
			value = ""
		}
		value = value.replace(/\D/g, "");
		return !helpers.req(value) || validateCPF(value);
	}
);
customValidators.cnpjValidCheck = () => helpers.withParams(
	{ type: 'cnpjValidCheck' },
	function (value) {
		if(!value) {
			value = ""
		}
		value = value.replace(/\D/g, "");
		return !helpers.req(value) || validateCNPJ(value);
	}
);

export default customValidators
