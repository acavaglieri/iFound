import { Ability } from "@casl/ability";

export function getAbilities(role) {
    role = localStorage.getItem('role');
    var abilities = [];
    switch(role) {
        case 'admin':
            abilities.push({ action: 'view', subject: 'users' });
            abilities.push({ action: 'edit', subject: 'users' });
            abilities.push({ action: 'remove', subject: 'users' });
            abilities.push({ action: 'add', subject: 'users' });

            abilities.push({ action: 'view', subject: 'apis' });
            abilities.push({ action: 'edit', subject: 'apis' });
            abilities.push({ action: 'remove', subject: 'apis' });
            abilities.push({ action: 'add', subject: 'apis' });

            abilities.push({ action: 'view', subject: 'defaultWorkspace' });
    }
    return abilities;
}
export const abilitiesReturn = getAbilities();
export default new Ability(getAbilities());
