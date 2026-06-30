# Evidence-Anchored KV Eviction for Long Agent Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-anchored-kv-eviction-for-long-agent-context-4c316da68b0a`
Run ID: `evidence-anchored-kv-eviction-for-long-agent-context-4c316da68b0a-20260613T101831961967+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/274266e08693

## What looked useful

Evidence anchoring produced mean success 0.875 and mean recall 0.979 in clean-anchor synthetic calibration, versus 0.750/0.846 for attention-proxy and 0.000/~0.048 for recency/random. Under noisy anchors at budget 64, evidence anchoring retained mean recall 0.771 versus 0.401 for attention-proxy, but full-answer success was only 0.122.

## Boundaries and scale limits

No real transformer KV cache, no real agent traces, no latency or GPU-memory measurements, and only 20 clean-anchor trials per full-grid setting plus 30 noisy-anchor trials at budget 64. The 100-trial confirmation was terminated after crossing the CPU-only time ceiling.

## Claim scope

Synthetic cache-policy mechanism test: evidence-anchored eviction preserves answer-critical synthetic evidence better than recency/random and improves over an attention-proxy baseline only under tight cache budgets or noisy-anchor recall metrics.

## Why it stopped

Proxy-only useful signal with mixed evidence; not a full validation and not paper-ready.

## Recommended next action

Stop this worker run; the next concrete step is a real-model KV-cache or serving-simulator evaluation on long-context QA/agent traces with measured memory, latency, answer accuracy, and anchor-quality ablations.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model KV-cache evidence-anchor eviction on long-context QA traces
- Success threshold: At matched cache budgets, evidence-anchor eviction improves answer accuracy by at least 5 percentage points over the strongest non-anchor eviction baseline while keeping retained-evidence recall higher and latency overhead under 10%.
- Stop condition: Stop if evidence-anchor eviction fails to beat the strongest non-anchor baseline on answer accuracy or requires high-quality anchors that are unavailable in realistic traces.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-anchored-kv-eviction-for-long-agent-context-4c316da68b0a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
