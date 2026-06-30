# Evidence-Ledger Agent with Local NLI Rollback

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-agent-with-local-nli-rollback-63f1897b2a54`
Run ID: `evidence-ledger-agent-with-local-nli-rollback-63f1897b2a54-20260531T231108491082+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4b1cd1e04538

## What looked useful

The mechanism test showed baseline accuracy 0.667 versus ledger accuracy 1.000 on 240 synthetic cases. The ledger fixed all 80 low-quality contradiction cases and did not roll back any of 80 valid high-reliability correction cases. A model-backed NLI smoke attempt timed out after 300 seconds without metrics.

## Boundaries and scale limits

Completed runs used deterministic local lexical contradiction over extracted evidence records, not a neural NLI model; data were synthetic with 240 cases and three evidence statements per case; no real retrieval-agent workload, paraphrase stress test, or latency/memory profile for a loaded NLI model was completed.

## Claim scope

On synthetic canonical slot-value evidence streams, an evidence ledger with reliability-aware rollback rejects lower-reliability contradictory updates and preserves higher-reliability corrections, improving final-answer accuracy over a latest-claim baseline.

## Why it stopped

This run is closed as a no-paper useful signal because the completed evidence validates only the ledger rollback policy under canonicalized synthetic extraction; the local neural NLI component did not complete and therefore the original full idea is not directly validated.

## Recommended next action

Run a bounded deepen test with a pre-fetched or locally cached neural NLI model on paraphrased evidence pairs and a no-reliability ablation before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural NLI paraphrase stress test for evidence-ledger rollback
- Success threshold: On at least 300 paraphrased synthetic streams, neural-NLI rollback improves final-answer accuracy by at least 15 percentage points over latest-claim baseline, keeps valid-correction false rollback rate below 5%, and reports p95 rollback-decision latency under 250 ms on the local host.
- Stop condition: Stop if the NLI model cannot be loaded locally within 10 minutes, contradiction recall is below 80% on paraphrased low-quality contradictions, or valid-correction false rollback rate is 10% or higher.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-with-local-nli-rollback-63f1897b2a54`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
