# Home Distributed Training Toy Proof: Bounded-Comms Adam

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `home-distributed-training-toy-proof-bounded-comms-adam-c77b6804e3aa`
Run ID: `home-distributed-training-toy-proof-bounded-comms-adam-c77b6804e3aa-20260610T075611844785+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b5322e31cb5c

## What looked useful

At roughly 1.95% of full-sync communication, sparse error-feedback Adam deltas often had lower loss than local Adam averaged every 50 steps at roughly 2% communication. At roughly 10% communication, local Adam averaged every 10 steps consistently had the best loss across IID/non-IID scenarios and lr values 0.004, 0.008, and 0.016. The tested sparse bounded-comms Adam mechanism is plausible under severe bandwidth constraints but not a clear improvement over a simple tuned baseline.

## Boundaries and scale limits

No real home network, asynchronous execution, deep neural network, transformer, GPT-2-small-class baseline, or datacenter-scale training was tested. The dense full-sync Adam control was not exhaustively tuned and underperformed in this toy setup, so conclusions should emphasize matched-byte bounded methods rather than full-sync superiority.

## Claim scope

On a synthetic distributed logistic-regression toy task with 8 simulated workers, 5 seeds, IID and non-IID client distributions, and three learning rates, sparse top-k error-feedback Adam deltas are competitive at very low communication ratios but do not reliably outperform periodic local Adam averaging at matched byte budgets.

## Why it stopped

No-paper closure: the proxy experiment found a useful but mixed signal rather than a paper-ready positive result.

## Recommended next action

Run a bounded small-neural-task follow-up with matched communication budgets and tuned periodic-local baselines; do not write a paper from this toy result alone.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Matched-byte sparse Adam vs periodic local Adam on a small neural task
- Success threshold: Sparse error-feedback Adam must improve final validation loss by at least 2% relative versus the best tuned periodic local Adam baseline at the same communication budget in both IID and non-IID settings.
- Stop condition: Stop as negative if sparse error-feedback Adam does not beat periodic local Adam at matched bytes after tuning, or if gains appear only in one seed/scenario.

## Evidence references

- Artifact root: `<local-path>/projects/home-distributed-training-toy-proof-bounded-comms-adam-c77b6804e3aa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
