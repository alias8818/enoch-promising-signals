# Small-LM serving test for context-routed n-gram speculative decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `small-lm-serving-test-for-context-routed-n-gram-speculativ-d86d93eca2`
Run ID: `small-lm-serving-test-for-context-routed-n-gram-speculativ-d86d93eca2-20260526T143011288696+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Context-Aware N-gram Speculative Decoding: enoch://control-plane/projects/context-aware-n-gram-speculative-decoding-cfd239152dc8/runs/context-aware-n-gram-speculative-decoding-cfd239152dc8-20260526T020851382698+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2d456810f23e

## What looked useful

Routed n-gram speculative decoding achieved 3.0x estimated model-call speedup versus 2.6x for a global n-gram table and 1.2x for a deliberately misrouted control, with exact greedy output preserved on all 18 prompts.

## Boundaries and scale limits

Synthetic controlled prompts, small n-gram memories, one small LM, 24 generated tokens per prompt, no production KV-cache scheduler, no batching stress, and no real traffic trace.

## Claim scope

In a controlled 18-prompt small-LM serving harness using distilgpt2 as the oracle, context-routed n-gram draft tables preserved exact greedy output and reduced oracle verification calls more than a mixed global n-gram table.

## Why it stopped

Tier 1 mechanism threshold was met, but the result is a controlled small direct test rather than publication-grade serving evidence.

## Recommended next action

Run a deeper local confirmation on a realistic mixed-domain prompt corpus with KV-cache-aware verification and report acceptance, latency, and throughput against global n-gram and no-draft baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache-aware routed n-gram speculative decoding on realistic mixed-domain prompts
- Success threshold: Routed decoding must preserve exact output on every prompt and improve p90 latency or oracle-call-adjusted throughput by at least 10% over the global n-gram baseline while beating the misrouted control.
- Stop condition: Stop if routed decoding fails exact-output preservation, fails to beat global n-gram by 10% on both latency and oracle-call efficiency, or if realistic prompts do not produce enough repeatable n-gram draft opportunities for a fair test.

## Evidence references

- Artifact root: `<local-path>/projects/small-lm-serving-test-for-context-routed-n-gram-speculativ-d86d93eca2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
