// Public config

var antiCapthaPredefinedApiKey = 'fe5e06bc8ba3b0d4d5c7222b8b8e7a71';

var defaultConfig = {
    // settings
    enable: true,
    account_key: antiCapthaPredefinedApiKey,
    auto_submit_form: false,
    play_sounds: false,

    where_solve_list: [],
    where_solve_white_list_type: false, // true -- considered as white list, false -- black list

    solve_recaptcha2: true,
    solve_recaptcha3: false,
    recaptcha3_score: 0.9,
    solve_invisible_recaptcha: false,
    solve_funcaptcha: false, // off by default
    solve_geetest: true,
    solve_hcaptcha: false,
    use_predefined_image_captcha_marks: true,

    solve_proxy_on_tasks: false,
    user_proxy_protocol: 'HTTP',
    user_proxy_server: '',
    user_proxy_port: '',
    user_proxy_login: '',
    user_proxy_password: '',

    use_recaptcha_precaching: true,
    k_precached_solution_count_min: 10,
    k_precached_solution_count_max: 10,

    dont_reuse_recaptcha_solution: true,
    start_recaptcha2_solving_when_challenge_shown: false,
    solve_only_presented_recaptcha2: false,

    // use_recaptcha_accelerator: false,

    // status
    account_key_checked: antiCapthaPredefinedApiKey ? true : false, // set after account_key check
    free_attempts_left_count: 15 // move to config
};