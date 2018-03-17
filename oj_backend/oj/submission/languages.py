

c_lang_config={
    "compile":{
        "src_name":"main.c",
        "exe_name":"main",
        "max_cpu_time":3000,
        "max_real_time":5000,
        "max_memory":1024*1024*128,
        "compile_command":"/usr/bin/gcc -DONLINE_JUDGE -O2 -w -fmax-errors=3 -std=c99 {src_path} -lm -o {exe_path}",
    },
    "run":{
        "command":"{exe_path}",
        "seccomp_rule":"c_cpp",
        "env":["LANG=en_US.UTF-8","LANGUAGE=en_US:en","LC_ALL=en_US.UTF-8"]
    }
}