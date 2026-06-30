# Causal generation test for anchor-gated KV compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `causal-generation-test-for-anchor-gated-kv-compression-ba8015a338`
Run ID: `causal-generation-test-for-anchor-gated-kv-compression-ba8015a338-20260531T101642316469+0000`

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

- Parent run decision: Anchor-Gated KV Cache Compression: enoch://control-plane/projects/anchor-gated-kv-cache-compression-6e6d8b46b92a/runs/anchor-gated-kv-cache-compression-6e6d8b46b92a-20260530T060113392096+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/daf43b4f85d4

## What looked useful

Anchor+recent compression had mean NLL 3.7078 versus dense 3.4686 and recency-only 7.8901, beating recency on 24/24 samples. However, first16+recent matched anchor+recent at mean NLL 3.7084, so the evidence supports prefix/anchor retention but not a distinct attention-gated advantage.

## Boundaries and scale limits

Single pretrained GPT-2 model, WikiText-2 only, 24 samples, 128-token prompts, 64-token continuations, inference-only Python cache manipulation, no learned gate, no long-context or serving-kernel benchmark.

## Claim scope

On GPT-2 small with WikiText-2 128-token prompts and 64-token teacher-forced continuations, retaining 16 prompt anchor/prefix positions plus recent KV positions at a 64-position cache budget preserves next-token NLL far better than recency-only KV compression.

## Why it stopped

Tier 1 direct test completed; result is useful but mixed because the proposed attention anchor gate did not beat the simple first-token anchor control, so it is no-paper evidence rather than paper-positive support.

## Recommended next action

Run a bounded deepen follow-up over longer contexts and multiple cache budgets to test whether attention-selected anchors ever outperform fixed first-token retention by at least 0.05 NLL while preserving dense-logit agreement.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Longer-context budget sweep for attention anchors versus fixed prefix anchors
- Success threshold: Attention-selected anchors beat first-prefix anchors by at least 0.05 mean NLL and improve dense top-1 agreement by at least 0.02 in at least two longer-context budget settings, while beating recency-only in at least 90% of samples.
- Stop condition: Stop if attention-selected anchors remain within +/-0.02 NLL of first-prefix anchors across the first two longer-context settings or fail to beat recency-only in more than 10% of samples.

## Evidence references

- Artifact root: `<local-path>/projects/causal-generation-test-for-anchor-gated-kv-compression-ba8015a338`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
