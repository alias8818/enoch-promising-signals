# Speculative Decoding with 2-bit Draft Model and Channel Residual Compensation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `speculative-decoding-with-2-bit-draft-model-and-channel-residual-compensation-992034b0722a`
Run ID: `speculative-decoding-with-2-bit-draft-model-and-channel-residual-compensation-992034b0722a-20260613T185051081535+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/faf8d73e53c5

## What looked useful

Logit-channel residual compensation improved expected acceptance overlap from 0.800030 to 0.810850, a +0.010820 absolute delta, positive on 12/12 paired seeds with approximate 95% CI [0.010247, 0.011392]. KL(target || draft) improved from 0.129945 to 0.115900.

## Boundaries and scale limits

The run used 12 synthetic seeds, 4096 calibration contexts and 8192 eval contexts per seed on a CPU worker. It did not use a trained GPT-class transformer, a separately trained draft model, an int2 serving kernel, or wall-clock speculative decoding throughput measurements.

## Claim scope

In a synthetic fixed MLP language-model proxy, a calibrated channel residual correction for a 2-bit draft improves exact expected speculative acceptance overlap versus naive 2-bit quantization.

## Why it stopped

No-paper useful signal: this was a bounded synthetic distribution-overlap proxy, not full validation of a deployable speculative decoding method.

## Recommended next action

Run a bounded deepen follow-up on a trained GPT-2-small-class or tiny transformer target/draft pair, measuring acceptance overlap and real speculative decoding throughput with residual overhead included.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train a Small Transformer Draft to Test Int2 Channel Residual Compensation in Real Speculative Decoding
- Success threshold: At least +0.5 percentage points absolute acceptance-overlap improvement over naive int2 and at least 5% end-to-end tokens/sec improvement over naive int2 speculative decoding on the same target/draft setup, with no degradation in verification-correct output sampling.
- Stop condition: Stop if channel residual variants fail to improve acceptance overlap over naive int2 on held-out data, or if measured residual overhead eliminates end-to-end throughput gain.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-with-2-bit-draft-model-and-channel-residual-compensation-992034b0722a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
