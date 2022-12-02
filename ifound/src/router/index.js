import Vue from "vue";
import Router from "vue-router";
import layout from "../layout";

Vue.use(Router);

const router = new Router({
  linkExactActiveClass: "active",
  scrollBehavior: () => ({ y: 0 }),
  mode: "history",
  base: "../",
  routes: [
    {
      path: "/",
      name: "website_home",
      component: () => import("@/pages/website-page/PlgWebsite.vue"),
      meta: { requiresAuth: false }
    },
    {
      path: "/login",
      name: "login",
      component: () => import("@/pages/auth-pages/login"),
      meta: { requiresAuth: false }
    },
    {
      path: "/register",
      name: "register",
      component: () => import("@/pages/auth-pages/register"),
      meta: { requiresAuth: false }
    },
    {
      path: "/forgot/password",
      name: "forgot_password",
      component: () => import("@/pages/auth-pages/PlgResetPassword"),
      meta: { requiresAuth: false }
    },
    {
      path: "/forgot/password/sent",
      name: "forgot_password_sent",
      component: () => import("@/pages/auth-pages/PlgResetPasswordSent"),
      meta: { requiresAuth: false }
    },
    {
      path: "/user/register/success",
      name: "user_confirm_email_sent_warning",
      component: () => import("@/pages/auth-pages/PlgConfirmationEmailSent"),
      meta: { requiresAuth: false }
    },
    {
      path: "/user/confirm",
      name: "user_confirm",
      component: () => import("@/pages/auth-pages/PlgConfirmUser"),
      meta: { requiresAuth: false }
    },
    {
      path: "/secure",
      name: "secure",
      component: () => import("@/views/secure.vue"),
      meta: { requiresAuth: false }
    },
    {
      path: "/auth-pages",
      component: {
        render(c) {
          return c("router-view");
        }
      },
      children: [
        // {
        //   path: "login",
        //   name: "login",
        //   component: () => import("@/pages/auth-pages/login")
        // },
        //{
        //  path: "register",
        //  name: "register",
        //  component: () => import("@/pages/auth-pages/register")
        //},
      ]
    },
    {
      path: "/error-pages",
      component: {
        render(c) {
          return c("router-view");
        }
      },
      children: [
        {
          path: "error-404",
          name: "error-404",
          component: () => import("@/pages/error-pages/error-404")
        },
        {
          path: "error-500",
          name: "error-500",
          component: () => import("@/pages/error-pages/error-500")
        }
      ]
    },
    {
      path: "*",
      redirect: "/error-404",
      component: {
        render(c) {
          return c("router-view");
        }
      },
      children: [
        {
          path: "error-404",
          component: () => import("@/pages/error-pages/error-404")
        }
      ]
    },
    {
      path: "/site",
      component: layout,
      children: [
        {
          path: "home",
          name: "home",
          component: () => import("@/pages/home-page/PlgHome"),
          meta: { requiresAuth: true }
        },
        {
          path: "profile",
          name: "user_profile",
          component: () => import("@/pages/profile-pages/PlgUserProfile"),
          meta: { requiresAuth: true }
        },
        {
          path: "animais",
          name: "animais",
          component: () => import("@/pages/profile-pages/Animais"),
          meta: { requiresAuth: true }
        },
        {
          path: "animais/info",
          name: "animais_info",
          component: () => import("@/pages/profile-pages/PlgTransactionInfo"),
          meta: { requiresAuth: true }
        },
        {

          path: "payments",
          name: "payments_table",
          component: () => import("@/pages/payments-pages/PlgPayments"),
          meta: { requiresAuth: true }
        },
        {
          path: "payments/new",
          name: "payments_new",
          component: () => import("@/pages/payments-pages/PlgPayment"),
          meta: { requiresAuth: true }
        },
        {
          path: "payments/:id/edit",
          name: "payments_edit",
          component: () => import("@/pages/payments-pages/PlgPayment"),
          meta: { requiresAuth: true }
        },
        {
          path: "settings",
          name: "settings",
          component: () => import("@/pages/admin-pages/PlgSettings"),
          meta: { requiresAuth: true }
        },
        {
          path: "accounts",
          name: "accounts",
          component: () => import("@/pages/PlgAccounts"),
          meta: { requiresAuth: true }
        },
        {
          path: "accounts/:id",
          name: "accounts/:id",
          component: () => import("@/pages/PlgAccount"),
          meta: { requiresAuth: true }
        },
        {
          path: "account_addresses/:id",
          name: "account_addresses/:id",
          component: () => import("@/pages/PlgAccountAddress"),
          meta: { requiresAuth: true }
        },
        {
          path: "accounts/:id/edit",
          name: "accounts/:id/edit",
          component: () => import("@/pages/PlgAccount"),
          meta: { requiresAuth: true }
        },
        {
          path: "users",
          name: "users",
          component: () => import("@/pages/users-pages/PlgUsers"),
          meta: { requiresAuth: true }
        },
        {
          path: "users/:id/edit",
          name: "users_edit",
          component: () => import("@/pages/users-pages/PlgUser"),
          meta: { requiresAuth: true }
        },
        {
          path: "users/add",
          name: "users_add",
          component: () => import("@/pages/users-pages/PlgUser"),
          meta: { requiresAuth: true }
        },
        {
          path: "api_logs_docs",
          name: "api_logs_docs",
          component: () => import("@/pages/PlgApiLogsDocs"),
          meta: { requiresAuth: true }
        },
        {
          path: "api_logs",
          name: "api_logs",
          component: () => import("@/pages/PlgApiLogs"),
          meta: { requiresAuth: true }
        },
      ]
    },
  ]
});

router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && localStorage.getItem('authenticated') == "false") {
    router.replace({name: 'login'})
  } else if (!to.meta.requiresAuth && localStorage.getItem('authenticated') == "true") {
    router.replace({name: 'home'})
  } 
  else {
    next();
  }
});

export default router
