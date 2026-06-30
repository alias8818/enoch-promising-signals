# Context Suffix-Match Variable-Length Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `context-suffix-match-variable-length-speculative-decoding-a5b6bb16a3ef`
Run ID: `context-suffix-match-variable-length-speculative-decoding-a5b6bb16a3ef-20260528T192621258851+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/8228255b12eb

## What looked useful

The mechanism is real but repetition-dependent. No repeated structure produced no benefit; synthetic repeat probability 0.02 to 0.20 increased best ideal speedup from 1.404x to 3.109x. Prompt repetition and EOS left-padding can severely inflate results, so future evaluations must avoid those confounds. Simple variable-length policies improved acceptance versus long fixed drafts but did not dominate fixed lengths under raw-call or simple verifier-cost metrics.

## Boundaries and scale limits

Small local traces only: synthetic repetition probes and greedy distilgpt2 continuations. No wall-clock serving benchmark, no KV-cache/kernel overhead measurement, no multi-model robustness, no quality-preserving stochastic decode validation, and no comparison to production speculative decoding systems.

## Claim scope

On online-only token traces, context suffix-copy drafting can reduce ideal target verification calls when the trace contains repeated spans; in a corrected 16 x 192-token greedy distilgpt2 trace, fixed 16-token suffix drafting reached 3.000x ideal call speedup, while tested variable-length suffix policies reached 2.049x to 2.603x and did not beat fixed-length controls.

## Why it stopped

Proxy/local trace evidence supports suffix-match drafting but not the specific variable-length superiority claim; this is not full validation or paper-grade serving evidence.

## Recommended next action

Stop this run as no-paper useful signal; a bounded follow-up should implement a real verifier-cost-aware adaptive draft policy inside an actual model speculative decoding loop and compare wall-clock tokens/sec against fixed n-gram drafting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Verifier-cost-aware adaptive suffix drafting in a real speculative decoding loop
- Success threshold: Adaptive policy improves wall-clock tokens/sec by at least 10% over the best fixed-length suffix baseline on both models while preserving exact target outputs and avoiding regressions on low-repetition prompts.
- Stop condition: Stop if adaptive policy fails to beat the best fixed baseline on wall-clock throughput, or if draft construction overhead cancels ideal call reductions on either model.

## Evidence references

- Artifact root: `<local-path>/projects/context-suffix-match-variable-length-speculative-decoding-a5b6bb16a3ef`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
