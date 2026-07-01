# N-gram speculative draft reduces local cascade latency

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-draft-reduces-local-cascade-latency-2fe4dca02186`
Run ID: `n-gram-speculative-draft-reduces-local-cascade-latency-2fe4dca02186-20260522T160254362352+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/bab4ca2ce6b9

## What looked useful

N-gram speculative drafting can reduce local target-model calls and latency when accepted spans are multi-token: distilgpt2 ngram=2 reached 2.36x median speedup across 15 cases, with exact output matches and 12/15 faster cases. It can also slow decoding: structured_json regressed to 0.70x-0.98x because speculative calls plus recompute gave 66 target calls versus 65 baseline.

## Boundaries and scale limits

Tested only distilgpt2 and sshleifer/tiny-gpt2 with greedy decoding, one local GPU process, short 64-item generations, synthetic/prompted repeated text, and a Python/Hugging Face implementation. Did not test true multi-model cascades, 7B+ targets, production inference engines, batching, quantization, sampling, or real traffic.

## Claim scope

In a local CUDA distilgpt2 greedy-decoding benchmark over five prompt classes, deterministic n-gram draft verification preserved exact greedy outputs and reduced latency when prompts induced multi-token repeated continuations, but regressed on a structured JSON case where rejection/recompute overhead outweighed call reduction.

## Why it stopped

Bounded local evidence supports the mechanism but is not broad or direct enough for a paper-positive local-cascade claim; this is a small-model greedy benchmark, not full cascade validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded step is to implement a cheap online gate for expected accepted span length and verify that it keeps the speedup cases while avoiding the structured_json regression.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Gated n-gram speculative decoding for local greedy generation
- Success threshold: Across at least 30 short greedy-decoding cases on a GPT-2-class or larger local target, gated n-gram speculation has median speedup above 1.5x on repeated-pattern prompts and no more than 5% median regression on non-repetitive or structured prompts, with exact token equality to baseline.
- Stop condition: Stop if the gate cannot predict regressions better than always-on speculation, or if avoiding regressions removes the majority of speedup on repeated-pattern prompts.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-draft-reduces-local-cascade-latency-2fe4dca02186`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
