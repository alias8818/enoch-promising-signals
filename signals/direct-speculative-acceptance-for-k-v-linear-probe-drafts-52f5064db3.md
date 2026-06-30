# Direct speculative acceptance for K/V linear probe drafts

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `direct-speculative-acceptance-for-k-v-linear-probe-drafts-52f5064db3`
Run ID: `direct-speculative-acceptance-for-k-v-linear-probe-drafts-52f5064db3-20260526T191451277658+0000`

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

- Parent run decision: KV-Cache Linear Probe Drafting: enoch://control-plane/projects/kv-cache-linear-probe-drafting-c7dd87616b44/runs/kv-cache-linear-probe-drafting-c7dd87616b44-20260525T125641553934+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/40dd4190e197

## What looked useful

Late-layer K/V features carried enough next-token information for a linear draft head to exceed the predeclared Tier 1 threshold: layer 5 confirmation reached 0.2610 exact acceptance, 0.1178 absolute lift over unigram, and 0.2686 target top-1 match on 2048 held-out positions.

## Boundaries and scale limits

Evidence is limited to a small frozen model, offline probe training, one-token acceptance, and distribution-level acceptance metrics. It does not validate multi-token speculative decoding, serving latency, cache integration overhead, robustness across datasets, or larger model behavior.

## Claim scope

In a Tier 1 small direct test on frozen distilgpt2 with WikiText-2 text, a linear probe over late-layer K/V activations produced a one-token draft distribution with exact speculative acceptance 0.2610 versus 0.1432 for a unigram baseline on 2048 held-out token positions.

## Why it stopped

Tier 1 direct evidence supports the mechanism, but the run is not paper-ready because it lacks full decode-loop, latency, baseline-cost, and larger-model validation.

## Recommended next action

Run a bounded deepen follow-up that implements a true multi-token speculative decode loop using the layer-5 K/V probe and compares accepted tokens per target pass plus wall-clock throughput against unigram and a small neural draft baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-token decode-loop validation for late-layer K/V linear probe drafts
- Success threshold: On at least 2048 generated token decisions, the K/V probe loop should preserve exact sampling correctness and improve accepted tokens per target pass by at least 25% over unigram while not being slower wall-clock than target-only greedy/sampling for the tested batch-1 setting.
- Stop condition: Stop if the full loop fails exactness checks, if probe overhead eliminates throughput gains, or if accepted tokens per target pass is within 10% of unigram after reproducing the one-token acceptance signal.

## Evidence references

- Artifact root: `<local-path>/projects/direct-speculative-acceptance-for-k-v-linear-probe-drafts-52f5064db3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
