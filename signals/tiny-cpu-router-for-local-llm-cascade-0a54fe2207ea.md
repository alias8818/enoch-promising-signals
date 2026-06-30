# Tiny CPU router for local LLM cascade

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiny-cpu-router-for-local-llm-cascade-0a54fe2207ea`
Run ID: `tiny-cpu-router-for-local-llm-cascade-0a54fe2207ea-20260525T045931403454+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/11a49bfa7e02

## What looked useful

Five seed runs completed in about 6.9 seconds each. Cheap-stage accuracy averaged 0.570; router test AUC averaged 0.818; at >=0.95 oracle-fallback cascade accuracy, accepted fraction averaged 0.349 and cost savings averaged 0.249. Router-only latency averaged p50 136 us/item and p95 251 us/item.

## Boundaries and scale limits

Proxy only: no real local LLMs, no generation tasks, no quantized model serving, oracle fallback labels, and a synthetic 10:1 cost model. Evidence does not establish production LLM cascade quality or latency.

## Claim scope

On a 20 Newsgroups text-classification proxy, a tiny CPU logistic router using cheap-model confidence and simple text statistics predicted cheap-stage correctness with mean test AUC 0.818 across five seeds. Under an oracle fallback and a 10:1 fallback-to-cheap cost model, it preserved at least 0.95 cascade accuracy while saving about 25% cost versus always using fallback.

## Why it stopped

Proxy evidence supports the mechanism but is insufficient for a paper or direct local LLM cascade claim.

## Recommended next action

Stop this run as no-paper proxy evidence; next run should directly evaluate the router on two local LLM or llama.cpp-compatible stages with labeled prompts and measured serving latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct local LLM cascade router evaluation
- Success threshold: At least 20% measured fallback latency or token-cost reduction versus always fallback while preserving at least 95% of always-fallback quality, with router overhead below 1 ms per prompt.
- Stop condition: Stop if router AUC is below 0.65 or no operating point achieves both 95% quality preservation and 10% measured cost/latency savings.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-cpu-router-for-local-llm-cascade-0a54fe2207ea`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
