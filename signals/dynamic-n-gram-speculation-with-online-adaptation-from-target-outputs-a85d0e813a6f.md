# Dynamic N-Gram Speculation with Online Adaptation from Target Outputs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `dynamic-n-gram-speculation-with-online-adaptation-from-target-outputs-a85d0e813a6f`
Run ID: `dynamic-n-gram-speculation-with-online-adaptation-from-target-outputs-a85d0e813a6f-20260603T155215132281+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/3f2a8595e547

## What looked useful

Natural streams showed 12.77%, 17.89%, and 13.28% dynamic target-call reductions versus greedy, while shuffled controls averaged only 1.17%. However, best fixed n3/k8 beat dynamic on all natural streams for raw target calls; dynamic only became favorable in a simple proposed-token verifier-cost proxy at alpha >= 0.02.

## Boundaries and scale limits

Trace-level proxy only: no actual LLM sampling, no transformer verifier kernels, no wall-clock serving latency, and only three public-domain/text corpora plus shuffled controls.

## Claim scope

On 120k-token real-text trace simulations, online n-gram caches built from previous target outputs reduce target calls on structured streams, but the tested dynamic UCB n/k selector does not beat the best fixed online n-gram baseline on raw target-call count.

## Why it stopped

Proxy/trace evidence is mixed: online adaptation works, but the dynamic policy is not directly superior to best fixed under the primary raw target-call metric.

## Recommended next action

Stop this run as no-paper useful signal; next run should measure actual small-LM speculative decoding latency against a validation-selected fixed n-gram baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-LM Wall-Clock Test for Dynamic Online N-Gram Speculation
- Success threshold: Dynamic online n-gram speculation achieves at least 5% lower end-to-end latency than the best fixed online n-gram baseline on both datasets with unchanged generated-token sequence under deterministic decoding.
- Stop condition: Stop if dynamic fails to beat best fixed latency on either dataset or if acceptance gains are erased by verifier overhead.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-n-gram-speculation-with-online-adaptation-from-target-outputs-a85d0e813a6f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
