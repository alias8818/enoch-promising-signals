# CPU Perplexity-Gated Model Cascade

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `68`
Project ID: `cpu-perplexity-gated-model-cascade-d7eed785fac9`
Run ID: `cpu-perplexity-gated-model-cascade-d7eed785fac9-20260524T192721104427+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `68`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/776b47d08011

## What looked useful

The larger proxy model improved average loss versus the smaller model, but prompt perplexity was a weak value gate: AUROC for predicting large-model improvement was 0.441, the best near-large threshold routed 89.8% of requests to the large model, beat random routing by only 0.00214 bits/char, and was only 0.524x as fast as always-large after gate overhead.

## Boundaries and scale limits

No transformer LLMs, no tokenizer-level serving traces, no batching/cache effects, no prompt-level task evaluation, and no 7B-class local inference. Results should not be read as a full CPU LLM cascade validation.

## Claim scope

Bounded CPU-only character n-gram proxy: raw prompt perplexity was tested as a request-level gate for routing target-token prediction between a small order-2 model and a larger order-3 model across five text domains.

## Why it stopped

Early proxy falsification: raw prompt perplexity detected some domain shift but did not provide a useful CPU cascade policy in the measured n-gram setup; this is not a full transformer-serving validation.

## Recommended next action

Stop this project as a no-paper useful negative; only reopen with a real CPU LLM serving trace that can test whether a learned/calibrated gate, not raw prompt perplexity alone, beats always-large and random routing on wall-clock latency and task quality.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/cpu-perplexity-gated-model-cascade-d7eed785fac9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
