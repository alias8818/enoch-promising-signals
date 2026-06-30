# KV-cache n-gram speculative decoding for a 300M-class GB10 target

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-n-gram-speculative-decoding-for-a-300m-class-gb10-9455e59737`
Run ID: `kv-cache-n-gram-speculative-decoding-for-a-300m-class-gb10-9455e59737-20260530T032051628572+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: N-gram speculative draft for 300M local target on GB10: enoch://control-plane/projects/n-gram-speculative-draft-for-300m-local-target-on-gb10-ade73dcbb47e/runs/n-gram-speculative-draft-for-300m-local-target-on-gb10-ade73dcbb47e-20260529T225651550105+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3ff0a491742f

## What looked useful

The mechanism is real in a bounded 300M-class GB10 test: useful n-gram prompt hits cut forward calls by 62.5%-87.5% and can raise throughput substantially. Correctness is parameter-sensitive: k=8 diverged on the natural control and tiny-model smoke showed length overshoot, so broad or paper-ready claims are not supported.

## Boundaries and scale limits

Only three prompts, 64 generated tokens, two timed repeats after warmup, one 355M model, no production serving stack, no batching, no long-context held-out corpus, and no custom exact verifier beyond the installed Transformers prompt_lookup_num_tokens path.

## Claim scope

On GB10 with a 355M GPT-2-medium target model, Transformers prompt-lookup n-gram assisted greedy decoding can reduce target forward calls and improve throughput on controlled prompts; k=4 preserved greedy output on three small prompts with 1.79x-2.86x speedup, while k=8 reached about 5x on repetition-heavy prompts but failed exactness on a natural control.

## Why it stopped

Tier 1 direct evidence produced a useful but mixed signal; correctness sensitivity prevents paper readiness from this run.

## Recommended next action

Run a bounded held-out exactness and k-sweep follow-up on 100+ copy/repetition and natural prompts for a 300M-500M target, using exact greedy-output equality as the first success gate.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out exactness k-sweep for 300M-class prompt-lookup decoding on GB10
- Success threshold: For one fixed k, at least 99% exact greedy-output equality, zero systematic length overshoot, and at least 1.5x median throughput improvement on copy-heavy prompts without slowing natural controls below baseline.
- Stop condition: Stop if all k values with at least 1.5x copy-heavy speedup have less than 99% exactness or any repeatable length overshoot on the held-out set.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-n-gram-speculative-decoding-for-a-300m-class-gb10-9455e59737`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
