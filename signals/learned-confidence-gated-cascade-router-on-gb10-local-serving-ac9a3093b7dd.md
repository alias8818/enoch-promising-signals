# Learned confidence-gated cascade router on GB10 local serving

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `learned-confidence-gated-cascade-router-on-gb10-local-serving-ac9a3093b7dd`
Run ID: `learned-confidence-gated-cascade-router-on-gb10-local-serving-ac9a3093b7dd-20260609T232641852706+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/de3914d62c41

## What looked useful

A logistic learned gate using margin, entropy, prompt length, retrieval match, and ambiguity features beat fixed confidence utility in all five seeds. Mean learned utility was 0.80270 versus 0.79712 for fixed confidence and 0.78061 for always-large; mean learned escalation rate was 0.62319 versus 0.65275 for fixed confidence.

## Boundaries and scale limits

The experiment did not measure real LLM outputs, real token-level latency, concurrent serving, production confidence calibration, or full workload diversity on GB10. It used 5,000 synthetic training requests and 20,000 held-out synthetic test requests per seed.

## Claim scope

Under a reproducible synthetic local-serving cascade trace with generated correctness, confidence, and latency surfaces, a learned confidence gate consistently improved latency-aware utility over fixed confidence thresholds and always-large serving across five seeds.

## Why it stopped

No-paper closure because the current result is synthetic/proxy evidence; it supports the routing mechanism but does not validate real GB10 LLM serving behavior.

## Recommended next action

Run a bounded direct-evidence follow-up with actual small and large local models on GB10, labeled prompts, confidence features, and measured latency under light concurrent serving.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Measured GB10 learned cascade routing with real local model traces
- Success threshold: Learned gate improves held-out latency-aware utility by at least 0.005 over the best fixed threshold baseline and keeps accuracy no more than 0.01 below that baseline across at least three random train/test splits.
- Stop condition: Stop if measured small-model confidence features fail to predict recoverable large-model errors better than fixed thresholds, or if learned-gate utility does not beat the best fixed threshold in at least two of three splits.

## Evidence references

- Artifact root: `<local-path>/projects/learned-confidence-gated-cascade-router-on-gb10-local-serving-ac9a3093b7dd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
