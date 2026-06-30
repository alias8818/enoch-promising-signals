# N-gram speculative decoding for CPU inference acceleration

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-decoding-for-cpu-inference-acceleration-693d6d76c65b`
Run ID: `n-gram-speculative-decoding-for-cpu-inference-acceleration-693d6d76c65b-20260529T070041071266+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/05ed41879930

## What looked useful

N-gram speculative decoding is mechanism-positive only under high exact-repetition conditions. For the tested natural text, exact continuation acceptance was too low: best ideal call-count speedup was 1.094x, below a stable 1.30x proxy cost for draft-length-1 verification.

## Boundaries and scale limits

No real LLM CPU serving runtime was benchmarked; verification latency was proxied with NumPy matrix multiplies, and model-generated outputs may have different repetition statistics than held-out corpus text.

## Claim scope

On a 50k-token held-out Tiny Shakespeare evaluation with exact n-gram draft tables, the best natural-text setting reduced target calls by 8.6% but did not support CPU acceleration under measured proxy verification costs; a synthetic repeated corpus showed the mechanism can accelerate when exact continuations recur frequently.

## Why it stopped

Proxy/direct-corpus evidence does not support the natural-text CPU acceleration claim; this is an early falsification of the practical speedup claim, not a full validation across real LLM serving stacks.

## Recommended next action

Stop this run as no-paper useful signal; run a direct llama.cpp CPU tokens/sec benchmark only if pursuing a bounded follow-up with real model verification.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct llama.cpp benchmark of n-gram speculative decoding on CPU
- Success threshold: At least 1.20x geometric-mean tokens/sec improvement over greedy decoding on natural prompts, with no prompt class below 0.95x and with synthetic repetition retained as a positive control.
- Stop condition: Stop if natural-prompt accepted tokens per call remains below 0.30 or measured tokens/sec is below baseline after lookup and verification overhead on two model sizes or prompt sets.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-decoding-for-cpu-inference-acceleration-693d6d76c65b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
