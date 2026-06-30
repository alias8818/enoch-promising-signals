# Acceptance-Rate Implicit Routing via Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `acceptance-rate-implicit-routing-via-speculative-decoding-147957572384`
Run ID: `acceptance-rate-implicit-routing-via-speculative-decoding-147957572384-20260524T212912580297+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/db549d6d1fbb

## What looked useful

Acceptance-rate routing improved future speculative acceptance over a fixed generalist by about +0.499 in separated domains and +0.234 in moderate domains, but underperformed the fixed generalist by about -0.026 even with 32 probes in the near-shared negative control.

## Boundaries and scale limits

Synthetic CPU-only simulation only; no real pretrained LMs, no real prompt corpus, no wall-clock serving throughput, no batching/KV-cache overhead, and no production speculative decoding stack were tested.

## Claim scope

Controlled Markov-LM simulation shows speculative accept/reject probes can route among specialist draft models when target domains are separated or moderately distinct, reaching near-oracle future acceptance with 8-32 probe tokens per specialist.

## Why it stopped

No-paper closure: this run produced a controlled mechanism signal plus a failure-mode control, but the evidence is synthetic/proxy-only and not publication-grade direct serving evidence.

## Recommended next action

Run a bounded real-LM follow-up using small target/draft models and domain-labeled prompts, measuring acceptance, target calls, latency, and output equivalence against generalist, metadata-router, random, and oracle baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-LM Acceptance-Probe Routing on Domain-Labeled Prompts
- Success threshold: Acceptance-probe routing beats the fixed generalist draft by at least 10% relative target-call reduction or latency improvement on separated/moderate domains, stays within 2% of oracle efficiency, preserves output equivalence, and does not beat the generalist on the near-shared negative control.
- Stop condition: Stop if probe overhead eliminates latency gains, routed acceptance fails to exceed the fixed generalist on separated/moderate domains, or output equivalence/quality changes materially.

## Evidence references

- Artifact root: `<local-path>/projects/acceptance-rate-implicit-routing-via-speculative-decoding-147957572384`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
