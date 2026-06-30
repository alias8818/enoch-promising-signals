# Joint INT2 Weight and KV-Cache Quantization with Shared Residual Codebook

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `joint-int2-weight-and-kv-cache-quantization-with-shared-residual-codebook-97eb31b161cf`
Run ID: `joint-int2-weight-and-kv-cache-quantization-with-shared-residual-codebook-97eb31b161cf-20260629T010747762624+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/640fda8882d3

## What looked useful

Shared same-K residual codebooks save half the centroid storage but caused about 2.2% higher mean reconstruction NMSE than separate K=16 codebooks and a 21.3% attention-error degradation in the mismatched weight-heavy/KV-smooth distribution. At equal codebook bytes, shared K=32 beat separate K=16 on overall linear relative MSE (0.3494 vs 0.3719) and attention relative MSE (0.2054 vs 0.2137).

## Boundaries and scale limits

No trained model, real model weights, real KV traces, perplexity, or serving latency were measured. Results are synthetic/proxy only with 15 medium cases across three distributions and K in {8,16,32}.

## Claim scope

Synthetic grouped INT2 quantization probe over weight-like matrices and KV-cache-like tensors. Same-size shared residual codebooks were worse than separate residual codebooks, but a larger shared codebook at equal codebook-storage budget improved proxy linear and attention errors versus two smaller separate codebooks.

## Why it stopped

Closed as no-paper useful signal because evidence is synthetic/proxy and mixed: same-size sharing is brittle, while the equal-storage larger shared codebook variant is promising enough for a bounded real-model follow-up.

## Recommended next action

Run a bounded real-activation deepen test on a GPT-2-small-class model: collect layerwise weight and KV residuals, compare separate K=16 against shared K=32 at equal codebook storage, and measure reconstruction plus perplexity deltas.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real GPT-2-small residual trace test for equal-storage shared residual codebooks
- Success threshold: Shared K=32 at equal codebook storage must be no worse than separate K=16 by more than 1% relative on mean reconstruction NMSE and no worse than 0.02 absolute next-token loss on the evaluated public text sample.
- Stop condition: Stop if shared equal-storage codebooks exceed either reconstruction or loss threshold on two or more representative layers, or if real KV trace collection cannot be completed locally within the bounded run.

## Evidence references

- Artifact root: `<local-path>/projects/joint-int2-weight-and-kv-cache-quantization-with-shared-residual-codebook-97eb31b161cf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
